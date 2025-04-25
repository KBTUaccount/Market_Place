from django.urls import path
from users.views import register, profile
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


app_name = "users"
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile')
]
