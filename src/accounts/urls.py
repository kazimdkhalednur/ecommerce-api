from rest_framework_simplejwt import views as jwt_views

from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
]
