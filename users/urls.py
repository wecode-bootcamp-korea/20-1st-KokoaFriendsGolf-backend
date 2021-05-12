from django.urls import path
from users.views import SignInView

urlpatterns = [
    path('/users/signin', SignInView.as_view()),
    path('/users/signup', SignUpView.as_view()),
]