from django.urls import path 
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import *


urlpatterns = [
    # Auth view sets
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('remember-me/', TokenRefreshView.as_view(), name='refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name='verify-token'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('profile/', UsreProfileAPIView.as_view(), name='profile'),
    
    # Reset password view sets
]
