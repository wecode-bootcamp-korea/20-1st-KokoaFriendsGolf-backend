import json
from json                       import JSONDecodeError

from django.views               import View
from django.utils.decorators    import method_decorator
from django.http.response       import JsonResponse

from products.models            import Product
from orders.models              import Order, OrderList, OrderStatus
from utils.decorators           import check_user, login_required

class OrderListView(View):
    ORDER_TYPES = ["IN_CART", "PURCHASE_INSTANT"]

    @method_decorator(check_user())
    def get(self, request):
        pass

    @method_decorator(login_required())
    def post(self, request):
        POSTABLE_ORDER_TYPES = ["IN_CART", "PURCHASE_INSTANT"]
        try:
            data            = json.loads(request.body)
            user            = request.user
            order_item_list = data['order_list']
            order_type      = data['order_type']

            if order_item_list == []:
                return JsonResponse({"status": "INVALID_ORDER", "message": f'Request must contain at least one order.'}, status=400)

            if order_type not in POSTABLE_ORDER_TYPES:
                return JsonResponse({"status": "ORDER_TYPE_ERROR", "message": f'Order type should be one of {POSTABLE_ORDER_TYPES}'}, status=400)

            self.init_order_types(POSTABLE_ORDER_TYPES)
            self.reset_orders(user)

            order_status = OrderStatus.objects.get(status=order_type)

            for order_item in order_item_list:
                quantity   = order_item['quantity']
                product_id = order_item['product_id']
                product    = Product.objects.get(id=product_id)
                new_order  = Order.objects.create(receiver_name = user.name, user = user, order_status = order_status)
                if OrderList.objects.filter(order__user = user).filter(product = product).filter(order__order_status__status = order_type).exists():
                    existing_order          = OrderList.objects.filter(order__user = user)\
                                                               .filter(product = product)\
                                                               .filter(order__order_status__status = order_type)[0]
                    existing_order_info     = existing_order.order
                    existing_order.quantity = quantity
                    existing_order.order    = new_order
                    existing_order.save()
                    existing_order_info.delete()

                else:
                    OrderList.objects.create(quantity=quantity, product=product, order=new_order)

            return JsonResponse({"status": "SUCCESS", "data": {"order_list": self.get_order_info(order_type_list=POSTABLE_ORDER_TYPES, user=user)}}, status=200)

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
                order.order.delete()

            if order_status.status == 'PURCHASE_CART':
                order_info              = order.order
                order_info.order_status = OrderStatus.objects.get(status = 'IN_CART')
                order_info.save()

        return

    def init_order_types(self, order_type_list):
        for order_type in order_type_list:
            if not OrderStatus.objects.filter(status=order_type).exists():
                OrderStatus.objects.create(status=order_type)
        return
    
    def get_order_info(self, order_type_list = [], user = None):
        if user:
            order_list = OrderList.objects.filter(order__user = user)\
                                          .filter(order__order_status__status__in = order_type_list)
        else:
            order_list = OrderList.objects.filter(order__order_status__status__in = order_type_list)
        
        order_info_list = []

        for order in order_list:
            order_info = {
                "id"          : order.id,
                "product_name": order.product.name,
                "quantity"    : order.quantity,
                "user"        : order.order.user.name,
                "status"      : order.order.order_status.status,
            }
            order_info_list.append(order_info)
        
        return order_info_list