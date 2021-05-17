from django.views           import View
from django.http.response   import JsonResponse
from django.utils.decorators import method_decorator

from products.models        import (Category, 
                                    SubCategory, 
                                    Product, 
                                    Character)
from utils.utils            import get_name_list, login_required

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

class ProductListView(View):
    @method_decorator(login_required())
    def get(self, request):
        order_by         = request.GET.get('orderBy', '-RECENT')
        cname            = request.GET.get('cname')
        search           = request.GET.get('search')
        products         = Product.objects.none()
        all_product_name = get_name_list(Product)
        product_list     = []

        if cname in [None, '']:
            products = Product.objects.all()
        
        if cname in get_name_list(Category):
            category      = Category.objects.get(name=cname)
            subcategories = SubCategory.objects.filter(category=category)
            products      = Product.objects.filter(subcategory__in = subcategories)

        if cname in get_name_list(SubCategory):
            products = Product.objects.filter(subcategory__name = cname)
            
        if cname in get_name_list(Character):
            products = Product.objects.filter(character__name = cname)
        
        if search is not None:
            for word in all_product_name:
                if search in word:
                    product_list.append(word)
            products = Product.objects.filter(name__in = product_list)
        
        if order_by == 'RECENT':
            products = products.order_by('-created_at')
            
        if order_by == '-RECENT':
            products = products.order_by('created_at')
            
        if order_by == 'PRICE':
            products = products.order_by('-price')
            
        if order_by == '-PRICE':
            products = products.order_by('price')
            
        if order_by == 'LIKE':
            products = sorted(products, key = lambda product: product.like_users.count(), reverse=True)

        if order_by == '-LIKE':
            products = sorted(products, key = lambda product: product.like_users.count())

        data = [product.get_info(exclude=["contents"]) for product in products]

        return JsonResponse({"status": "SUCCESS", "data": data}, status=200)