from django.views import View
from products.models import Product

class ProductListView(View):
    def get(self, request):
        pass

class ProductDetailView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

class CategoryView(View):
    def get(self, request):
        pass