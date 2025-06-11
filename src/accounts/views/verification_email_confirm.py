from drf_spectacular.utils import extend_schema, extend_schema_view, inline_serializer
from rest_framework import serializers as drf_serializers
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode
from utils.helpers import Response

from ..models import User
from ..tasks import send_verification_mail_task
from ..tokens import token_generator


@extend_schema_view(
    post=extend_schema(
        tags=["buyer"],
        responses={
            200: inline_serializer(
                name="VerificationEmailConfirmResponse",
                fields={
                    "message": drf_serializers.CharField(
                        default="Email verified Successfully and now you can login"
                    )
                },
            )
        },
    )
)
class VerificationEmailConfirmView(APIView):
    """Verification email confirm view"""

    authentication_classes = ()
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token, *args, **kwargs):
        user = self.get_user(uidb64)

        if user is None:
            return Response(
                status_code=status.HTTP_400_BAD_REQUEST, message="Invalid link"
            )

        if user.is_active:
            return Response(
                status_code=status.HTTP_200_OK,
                message="You are already verified your mail address",
            )

        if token_generator.check_token(user, token):
            user.is_active = True
            user.save(update_fields=["is_active"])
            return Response(
                status_code=status.HTTP_200_OK,
                message="Email verified Successfully and now you can login",
            )

        send_verification_mail_task(user.id, request)
        return Response(
            status_code=status.HTTP_201_CREATED,
            message="Verification timeout. A new mail send to your mail.",
        )

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            pk = User._meta.pk.to_python(uid)
            user = User._default_manager.get(pk=pk)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user
