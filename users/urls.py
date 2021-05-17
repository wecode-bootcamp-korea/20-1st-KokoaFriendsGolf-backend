from django.urls import path
from users.views import SignUpView, SignInView

urlpatterns = [
    path('/signin', SignInView.as_view()),
    path('/signup', SignUpView.as_view()),
]