from rest_framework_simplejwt import views as jwt_views

from django.urls import include, path

from . import views
from .buyer import urls as buyer_urls

app_name = "accounts"

urlpatterns = [
    path("", include(buyer_urls)),
    path("login/", views.TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
]
