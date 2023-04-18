# yourappname/urls.py
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *
from rest_framework import routers

urlpatterns = [
    ...,
    path('', include(router.urls)),
    
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),

    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]