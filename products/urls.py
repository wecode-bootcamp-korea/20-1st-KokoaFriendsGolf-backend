from django.urls    import path
from products.views import ProductDetailView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/<int:id>', ProductDetailView.as_view())
]
