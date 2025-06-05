from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers as drf_serializers
from rest_framework_simplejwt.views import TokenObtainPairView as JWTTokenObtainPairView

from .. import serializers
from ..models import User


@extend_schema(
    responses={
        200: inline_serializer(
            name="TokenObtainPairViewBuyerResponse",
            fields={
                "access": drf_serializers.CharField(),
                "refresh": drf_serializers.CharField(),
                "role": drf_serializers.CharField(default=User.UserRole.BUYER),
            },
        ),
    }
)
class TokenObtainPairView(JWTTokenObtainPairView):
    """
    Takes a set of user credentials and returns role, an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    serializer_class = serializers.TokenObtainPairSerializer
