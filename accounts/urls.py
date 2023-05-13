from django.urls import path
from .views import RegisterAPI, ProfileAPI, UserProfileAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('profile/<int:pk>', ProfileAPI.as_view(), name='profile'),
    path('profile/', UserProfileAPI.as_view(), name='profile'),
]
