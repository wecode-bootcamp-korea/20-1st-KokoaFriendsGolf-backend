from django.views             import View
from django.http              import JsonResponse
from django.core.exceptions   import ValidationError

from .models                  import (Category, SubCategory, Product, Character, 
                                     Review, Image, Option, Question, Answer)

class ProductListView(View):
    def get(self, request):
        ordering       = request.GET.get("sort", 0)
        category__name = request.GET["cname"]

        all_category       = Category.objects.all()
        category_name_list = []
        for categorys in all_category:
            category_name  = categorys.name
            category_name_list.append(category_name)

        all_sub_category       = SubCategory.objects.all()
        sub_category_name_list = []
        for sub_categorys in all_sub_category:
            sub_category_name  = sub_categorys.name
            sub_category_name_list.append(sub_category_name)

        if category__name in category_name_list: 
            category__id  = Category.objects.get(name=category__name).id
            category_all = SubCategory.objects.filter(category_id=category__id)
            category_products_list=[]
            for category_products in category_all:
                category_products_all = category_products.product_set.all()
                if ordering == 'high_price':
                    a = category_products_all.order_by('-price')
                if ordering == 'low_price':
                    a = category_products_all.order_by('price')
                if ordering == 0:
                    a = category_products_all.order_by('created_at')
                for category_product in a:
                    product_info = category_product.get_info()
                    del (product_info['contents'],
                         product_info['is_picked'],
                         product_info['subcategory'],
                         product_info['character'],
                         product_info['category'])
                    category_products_list.append(product_info)
            return JsonResponse({"products_list": category_products_list}, status=200)

        if category__name in sub_category_name_list:
            sub_category__id = SubCategory.objects.get(name=category__name).id
            sub_category = SubCategory.objects.get(id=sub_category__id)
            sub_category_products = sub_category.product_set.all()
            sub_category_products_list = []
            if ordering == 'high_price':
                a = sub_category_products.order_by('-price')
            if ordering == 'low_price':
                a = sub_category_products.order_by('price')
            if ordering == 0:
                a = sub_category_products.order_by('created_at')
            for sub_category_product in a:
                product_info = sub_category_product.get_info()
                del (product_info['contents'],
                     product_info['is_picked'],
                     product_info['subcategory'],
                     product_info['character'],
                     product_info['category'])
                sub_category_products_list.append(product_info)
            return JsonResponse({"products_list": sub_category_products_list}, status=200)

        if category__name =='0':
            products = Product.objects.all()
            products_list = []
            if ordering == 'high_price':
                a = products.order_by('-price')
            if ordering == 'low_price':
                a = products.order_by('price')
            if ordering == 0:
                a = products.order_by('created_at')
            for product in a:
                product_info = product.get_info()
                del (product_info['contents'],
                     product_info['is_picked'],
                     product_info['subcategory'],
                     product_info['character'],
                     product_info['category'])
                products_list.append(product_info)
            return JsonResponse({"products_list": products_list}, status=200)

        if category__name not in category_name_list:
            return JsonResponse ({"message": "NO CATEGORY"}, status=404)           

class CharacterListView(View):
    def get(self, request):
        character__name = request.GET['cname']
        ordering        = request.GET.get('sort', 0)

        all_character = Character.objects.all()
        character_name_list = []
        for characters in all_character:
            character_name = characters.name
            character_name_list.append(character_name)

        if character__name in character_name_list:
            one_character          = Character.objects.get(name=character__name)
            character_product_list = []
            character_products = one_character.product_set.all()
            if ordering == 'high_price':
                a = character_products.order_by('-price')
            if ordering == 'low_price':
                a = character_products.order_by('price')
            if ordering == 0:
                a = character_products.order_by('created_at')
            for character_product in a:
                product_info = character_product.get_info()
                del (product_info['contents'],
                     product_info['is_picked'],
                     product_info['subcategory'],
                     product_info['character'],
                     product_info['category'])
                character_product_list.append(product_info)
            return JsonResponse({"products_list": character_product_list}, status=200)

        if character__name not in character_name_list:
            return JsonResponse({"message": "NO CHARACTER"}, status=404)

