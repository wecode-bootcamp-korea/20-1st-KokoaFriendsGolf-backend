from django.urls import path
from users.views import SignUpView

urlpatterns = [
    path('/users/signup', SignUpView.as_view()),
]
