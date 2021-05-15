from django.views             import View
from django.http              import JsonResponse
from django.core.exceptions   import ValidationError

from .models                  import (Category, SubCategory, Product, Character, 
                                     Review, Image, Option, Question, Answer)

class ProductListView(View):
    def get(self, request):
        sub_category__id = request.GET.get("scid", 0)
        category__id     = request.GET.get("cid", 0)

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
                    product_info = {
                       "id"            : category_product.id,
                       "name"          : category_product.name,
                       "price"         : float(category_product.price),
                       "thumbnail_url" : category_product.thumbnail_url,
                       "is_new"        : False if not category_product.is_new else True,
                       "is_sale"       : False if not category_product.is_sale else True,
                       "is_soldout"    : False if not category_product.is_soldout else True,
                       "is_set"        : False if not category_product.is_set else True,
                       "discount_ratio": float(category_product.discount_ratio),
                       "created_at"    : category_product.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                       "updated_at"    : category_product.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                       }
                    category_products_list.append(product_info)
            return JsonResponse({"products_list": category_products_list}, status=200)

        if int(sub_category__id) in sub_category_id_list:
            sub_category = SubCategory.objects.get(id=sub_category__id)
            sub_category_products = sub_category.product_set.all()
            sub_category_products_list = []
            for sub_category_product in sub_category_products:
                product_info = {
                 "id"            : sub_category_product.id,
                 "name"          : sub_category_product.name,
                 "price"         : float(sub_category_product.price),
                 "thumbnail_url" : sub_category_product.thumbnail_url,
                 "is_new"        : False if not sub_category_product.is_new else True,
                 "is_sale"       : False if not sub_category_product.is_sale else True,
                 "is_soldout"    : False if not sub_category_product.is_soldout else True,
                 "is_set"        : False if not sub_category_product.is_set else True,
                 "discount_ratio": float(sub_category_product.discount_ratio),
                 "created_at"    : sub_category_product.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                 "updated_at"    : sub_category_product.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                 }
                sub_category_products_list.append(product_info)
            return JsonResponse({"products_list": sub_category_products_list}, status=200)

        if category__id == 0 and sub_category__id == 0:
            products = Product.objects.all()
            products_list=[]
            for product in products:
                product_info = {
                 "id"            : product.id,
                 "name"          : product.name,
                 "price"         : float(product.price),
                 "thumbnail_url" : product.thumbnail_url,
                 "is_new"        : False if not product.is_new else True,
                 "is_sale"       : False if not product.is_sale else True,
                 "is_soldout"    : False if not product.is_soldout else True,
                 "is_set"        : False if not product.is_set else True,
                 "discount_ratio": float(product.discount_ratio),
                 "created_at"    : product.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                 "updated_at"    : product.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                 } 
                products_list.append(product_info)
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
                    product_info = {
                     "id"            : character_product.id,
                     "name"          : character_product.name,
                     "price"         : float(character_product.price),
                     "thumbnail_url" : character_product.thumbnail_url,
                     "is_new"        : False if not character_product.is_new else True,
                     "is_sale"       : False if not character_product.is_sale else True,
                     "is_soldout"    : False if not character_product.is_soldout else True,
                     "is_set"        : False if not character_product.is_set else True,
                     "discount_ratio": float(character_product.discount_ratio),
                     "created_at"    : character_product.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                     "updated_at"    : character_product.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                     } 
                    character_product_list.append(product_info)
            return JsonResponse({"products_list": character_product_list}, status=200)

        if int(character__id) not in character_id_list:
            return JsonResponse({"message": "NO CHARACTER ID"}, status=400)

class SortView(View):
    def get(self, request):
        pass
