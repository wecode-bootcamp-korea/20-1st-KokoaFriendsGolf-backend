from django.http.response       import JsonResponse
from django.views               import View
from django.utils.decorators    import method_decorator

from products.models            import Product
from utils.decorators           import check_user, login_required

class ProductListView(View):
    def get(self, request):
        pass

class ProductDetailView(View):
    @method_decorator(check_user())
    def get(self, request, id):
        try:
            product      = Product.objects.get(id=id)
            user         = request.user
            product_info = product.get_info(user=user)
            return JsonResponse({'status': "SUCCESS", 'data':{'product': product_info}}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"status": "PRODUCT_NOT_FOUND", "message": "존재하지 않는 상품입니다."}, status=404)
    
    @method_decorator(login_required())
    def patch(self, request, id):
        try:
            product  = Product.objects.get(id=id)
            user     = request.user
            is_liked = product.get_info(user=user)['is_liked']

            if is_liked:
                product.like_users.remove(user)
            else:
                product.like_users.add(user)

            return JsonResponse({'status': "SUCCESS", 'message': f'is_liked changed to {product.get_info(user=user)["is_liked"]}'}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"status": "PRODUCT_NOT_FOUND", "message": "존재하지 않는 상품입니다."}, status=404)

class CategoryView(View):
    def get(self, request):
        pass
