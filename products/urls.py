from django.urls import path

from products.views import ProductDetailView

urlpatterns = [
    path('/<int:id>', ProductDetailView.as_view())
]
