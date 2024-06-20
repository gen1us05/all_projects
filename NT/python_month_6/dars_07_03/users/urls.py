from django.urls import path
from .views import UserLoginView, UserRegisterView, HomePageView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login_page'),
    path('register/', UserRegisterView.as_view(), name='register_page'),
    path('home/', HomePageView.as_view(), name='home_page')
]