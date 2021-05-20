import json

from json import JSONDecodeError
from os import name

from django.views import View
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse

from products.models import Product
from orders.models import Order, OrderList, OrderStatus
from utils.decorators import check_user, login_required


class OrderListView(View):
    ORDER_TYPES = ["IN_CART", "PURCHASE_INSTANT", "PURCHASE_CART", "PURCHASED"]

    @method_decorator(login_required())
    def get(self, request):
        user = request.user
        order_type = request.GET.get('orderType')
        order_list = []
        sum_total_origin_price = 0
        sum_total_discounted_price = 0
        sum_total_discount = 0

        if order_type not in self.ORDER_TYPES:
            return JsonResponse({"status": "INVALID_ORDER_TYPE_ERROR"}, status=401)

        order_items = OrderList.objects.filter(
            order__user=user, order__order_status__status=order_type)

        for product_info in order_items:
            order_product = {
                "order_id": product_info.order_id,
                "date": '2020-05-20',
                "name": product_info.product.name,
                "quantity": product_info.quantity,
                "origin_price": float(product_info.product.price),
                "discounted_price": float(product_info.product.price - (product_info.product.price * product_info.product.discount_ratio)),
                "thumbnail_url": product_info.product.thumbnail_url,
                "discount_ratio": float(product_info.product.discount_ratio),
                "total_discounted_price": float((product_info.product.price - (product_info.product.price * product_info.product.discount_ratio)) * product_info.quantity),
                "total_price": float(product_info.product.price * product_info.quantity),
                "total_discount": float(product_info.product.price * product_info.product.discount_ratio * product_info.quantity)
            }
            order_list.append(order_product)

        for order_list_dict in order_list:
            sum_total_origin_price += order_list_dict["total_price"]
            sum_total_discounted_price += order_list_dict["total_discounted_price"]
            sum_total_discount += order_list_dict["total_discount"]

            # return JsonResponse({'result': 'success'}, status=200)
        return JsonResponse(data={
            "status": "SUCCESS",
            "data": {
                "sum_total_origin_price": sum_total_origin_price,
                "sum_total_discounted_price": sum_total_discounted_price,
                "sum_total_discount": sum_total_discount,
                "final_price": sum_total_discounted_price + 3000,
                "shipping_fee": 3000,
                "product_list": order_list,
                "user_info": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "phone_number": user.phone_number,
                }
            }
        }, status=200)

    @ method_decorator(login_required())
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            product_id = data['product_id']
            quantity = data['quantity']
            order_type = data['order_type']
            product = Product.objects.get(id=product_id)

            if order_type not in self.ORDER_TYPES:
                return JsonResponse({"status": "ORDER_TYPE_ERROR", "message": f'Order type should be one of {self.ORDER_TYPES}'}, status=400)

            if product.is_soldout:
                return JsonResponse({"status": "INVALID_PRODUCT_ERROR", "message": f'Product id {product_id} is soldout'}, status=400)

            self.reset_orders(user)

            order_status = OrderStatus.objects.create(status=order_type)
            order = Order.objects.create(
                receiver_name=user.name, user=user, order_status=order_status)
            OrderList.objects.create(
                quantity=quantity, product=product, order=order)

            return JsonResponse({"status": "SUCCESS"}, status=200)

        except JSONDecodeError as e:
            return JsonResponse({"status": "JSON_DECODE_ERROR", "message": e.msg}, status=400)

        except KeyError as e:
            return JsonResponse({"status": "KEY_ERROR", "message": f'Key Error in Field "{e.args[0]}"'}, status=400)

        except Product.DoesNotExist:
            return JsonResponse({"status": "INVALID_PRODUCT_ERROR", "message": f'Product id {product_id} does not exist'}, status=401)

    def reset_orders(self, user):
        user_orders = OrderList.objects.filter(order__user=user)

        for order in user_orders:
            order_status = order.order.order_status

            if order_status.status == 'PURCHASE_INSTANT':
                order_status.delete()

            if order_status.status == 'PURCHASE_CART':
                order_status.status = 'IN_CART'
                order_status.save()

        return
