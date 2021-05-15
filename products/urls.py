from django.urls import path

from .views  import ProductListView, CharacterListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/character', CharacterListView.as_view())
]

