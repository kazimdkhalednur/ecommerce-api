from rest_framework_simplejwt import views as jwt_views

from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.BuyerSignUpView.as_view(), name="buyer-signup"),
    path("login/", views.TokenObtainPairView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
    path(
        "password-reset-mail/",
        views.PasswordResetMailView.as_view(),
        name="password_reset_mail",
    ),
    path(
        "otp-verify/",
        views.OTPVerifyView.as_view(),
        name="otp_verify",
    ),
    path(
        "password-reset/",
        views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password-change/",
        views.PasswordChangeView.as_view(),
        name="password_change",
    ),
]
