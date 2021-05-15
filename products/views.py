from django.views             import View
from django.http              import JsonResponse
from django.core.exceptions   import ValidationError

from .models                  import Category, SubCategory, Product, Character

class ProductListView(View):
    def get(self, request):
        sub_category__id = request.GET.get("scid", 0)
        category__id     = request.GET.get("cid", 0)
        character__id    = request.GET.get("chr_id", 0)

        all_category     = Category.objects.all()
        category_id_list = []
        for categorys in all_category:
            category_id = categorys.id
            category_id_list.append(category_id)

        all_sub_category     = SubCategory.objects.all()
        sub_category_id_list = []
        for sub_categorys in all_sub_category:
            sub_category_id = sub_categorys.id
            sub_category_id_list.append(sub_category_id)

        if int(category__id) in category_id_list:
            category_all = SubCategory.objects.filter(category_id=category__id)
            category_products_list=[]
            for category_products in category_all:
                category_products_all = category_products.product_set.all()
                for category_product in category_products_all:
                    category_product_information = {
                        'name'         : category_product.name, 
                        'price'        : category_product.price,
                        'thumbnail_url': category_product.thumbnail_url
                    }
                    category_products_list.append(category_product_information)
            return JsonResponse({"products_list": category_products_list}, status=200)

        if int(sub_category__id) in sub_category_id_list:
            sub_category = SubCategory.objects.get(id=sub_category__id)
            sub_category_products = sub_category.product_set.all()
            products_list = []
            for product in sub_category_products:
                product_information = {
                        'name' : product.name,
                        'price': product.price,
                        'thumbnail_url': product.thumbnail_url
                    }
                products_list.append(product_information)
            return JsonResponse({"products_list": products_list}, status=200)

        if category__id == 0 and sub_category__id == 0:
            products = Product.objects.all()
            products_list=[]
            for product in products:
                product_information = {
                        'name'         : product.name,
                        'price'        : product.price,
                        'thumbnail_url': product.thumbnail_url
                     }
                products_list.append(product_information)
            return JsonResponse({"products_list": products_list}, status=200)

        if int(category__id) not in category_id_list or int(sub_category__id) not in sub_category_id_list:
            return JsonResponse ({"message": "NO CATEGORY ID"}, status=400)           

class CharacterListView(View):
    def get(self, request):
        character__id    = request.GET.get('chr_id',0)

        all_character_id = Character.objects.all()
        character_id_list = []
        for characters in all_character_id:
            character_id = characters.id
            character_id_list.append(character_id)

        if int(character__id) in character_id_list:
            character_all          = Character.objects.filter(id=character__id)
            character_product_list = []
            for one_character in character_all:
                character_products = one_character.product_set.all()
                for character_product in character_products:
                    character_product_information = {
                                'name'         : character_product.name,
                                'price'        : character_product.price,
                                'thumbnail_url': character_product.thumbnail_url
                            }
                    character_product_list.append(character_product_information)
            return JsonResponse({"products_list": character_product_list}, status=200)

        if int(character__id) not in character_id_list:
            return JsonResponse({"message": "NO CHARACTER ID"}, status=400)
