import json
from json                       import JSONDecodeError

from django.views               import View
from django.utils.decorators    import method_decorator
from django.http.response       import JsonResponse

from products.models            import Product
from orders.models import Order, OrderList, OrderStatus
from utils.decorators           import check_user, login_required

class OrderListView(View):
    ORDER_TYPES = ["IN_CART", "PURCHASE_INSTANT", "PURCHASE_CART", "PURCHASED"]

    @method_decorator(check_user())
    def get(self, request):
        pass

    @method_decorator(login_required())
    def post(self, request):
        try:
            data       = json.loads(request.body)
            user       = request.user
            product_id = data['product_id']
            quantity   = data['quantity']
            order_type = data['order_type']
            product    = Product.objects.get(id=product_id)

            if order_type not in self.ORDER_TYPES:
                return JsonResponse({"status": "ORDER_TYPE_ERROR", "message": f'Order type should be one of {self.ORDER_TYPES}'}, status=400)
            
            if product.is_soldout:
                return JsonResponse({"status": "INVALID_PRODUCT_ERROR", "message": f'Product id {product_id} is soldout'}, status=400)
            
            self.reset_orders(user)

            order_status = OrderStatus.objects.create(status=order_type)
            order = Order.objects.create(receiver_name = user.name, user = user, order_status = order_status)
            OrderList.objects.create(quantity=quantity, product=product, order=order)

            return JsonResponse({"status": "SUCCESS"}, status=200)

        except JSONDecodeError as e: 
            return JsonResponse({"status": "JSON_DECODE_ERROR", "message": e.msg}, status=400)

        except KeyError as e:
            return JsonResponse({"status": "KEY_ERROR", "message": f'Key Error in Field "{e.args[0]}"'}, status=400)

        except Product.DoesNotExist:
            return JsonResponse({"status": "INVALID_PRODUCT_ERROR", "message": f'Product id {product_id} does not exist'}, status=401)
    
    def reset_orders(self, user):
        user_orders = OrderList.objects.filter(order__user = user)

        for order in user_orders:
            order_status = order.order.order_status
            
            if order_status.status == 'PURCHASE_INSTANT':
                order_status.delete()

            if order_status.status == 'PURCHASE_CART':
                order_status.status = 'IN_CART'
                order_status.save()

        return