from django.http.response import JsonResponse
from django.views    import View

from products.models import Product

class ProductListView(View):
    def get(self, request):
        pass

class ProductDetailView(View):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            product_info = product.get_info()
            return JsonResponse({'status': "SUCCESS", 'data':{'product': product_info}}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"status": "PRODUCT_NOT_FOUND", "message": "존재하지 않는 상품입니다."}, status=404)
            
class CategoryView(View):
    def get(self, request):
        pass
