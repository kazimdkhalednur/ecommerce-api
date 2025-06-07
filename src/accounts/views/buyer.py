from drf_spectacular.utils import extend_schema, extend_schema_view, inline_serializer
from rest_framework import serializers as drf_serializers
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from utils.helpers import Response

from ..serializers import BuyerSerializer


@extend_schema_view(
    post=extend_schema(
        tags=["buyer"],
        responses={
            201: inline_serializer(
                name="BuyerSignupResponse",
                fields={
                    "message": drf_serializers.CharField(
                        default="User created Successfully and check your mail inbox"
                    )
                },
            )
        },
    )
)
class BuyerSignUpView(CreateAPIView):
    """Buyer signup view"""

    authentication_classes = ()
    permission_classes = [AllowAny]
    serializer_class = BuyerSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response(
            status_code=status.HTTP_201_CREATED,
            message="User created Successfully and check your mail inbox",
        )
