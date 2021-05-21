from django.http.response    import JsonResponse
from django.views            import View
from django.utils.decorators import method_decorator

from products.models         import Product, Category, SubCategory, Character
from utils.decorators        import check_user, login_required
from utils.utils             import get_name_list


class ProductListView(View):
    LIMIT_DEFAULT  = 16
    OFFSET_DEFAULT = 0

    @method_decorator(check_user())
    def get(self, request):
        order_by         = request.GET.get('orderBy', '-RECENT')
        cname            = request.GET.get('cname')
        search           = request.GET.get('search')
        limit            = int(request.GET.get('limit', self.LIMIT_DEFAULT))
        offset           = int(request.GET.get('offset', self.OFFSET_DEFAULT))
        products         = Product.objects.none()
        all_product_name = get_name_list(Product)
        product_list     = []
        is_last_page     = True
        user             = request.user

        if cname in [None, '']:
            products = Product.objects.all()

        if cname in get_name_list(Category):
            products = Product.objects.filter(
                subcategory__category__name=cname)

        if cname in get_name_list(SubCategory):
            products = Product.objects.filter(subcategory__name=cname)

        if cname in get_name_list(Character):
            products = Product.objects.filter(character__name=cname)

        if search is not None:
            for word in all_product_name:
                if search in word:
                    product_list.append(word)
            products = Product.objects.filter(name__in=product_list)

        query_dict = {
            'RECENT' : '-created_at',
            '-RECENT': 'created_at',
            'PRICE'  : '-price',
            '-PRICE' : 'price'
        }
        products = products.order_by(query_dict[order_by])

        if order_by == 'LIKE':
            products = sorted(products, key=lambda product: product.like_users.count(), reverse=True)

        if order_by == '-LIKE':
            products = sorted(products, key=lambda product: product.like_users.count())

        if len(products) > (offset+limit):
            products     = products[offset:offset+limit]
            is_last_page = False
        else:
            products = products[offset:]

        data = [product.get_info(exclude=["contents"], user=user)
                for product in products]

        return JsonResponse({"status": "SUCCESS", "data": {"product_list": data, "is_last_page": is_last_page}}, status=200)


class ProductDetailView(View):
    @method_decorator(check_user())
    def get(self, request, id):
        try:
            product      = Product.objects.get(id=id)
            user         = request.user
            product_info = product.get_info(user=user)
            return JsonResponse({'status': "SUCCESS", 'data': {'product': product_info}}, status=200)

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