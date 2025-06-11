from rest_framework import serializers

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from ..models import Buyer, User
from ..tasks import send_verification_mail_task
from ..tokens import token_generator


class BuyerSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = Buyer
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password doesn't matched")
        data.pop("password2")
        return data

    def save(self, **kwargs):
        user = Buyer.objects.create_user(
            **self.validated_data, **kwargs, is_active=False
        )

        user_pk_bytes = force_bytes(User._meta.pk.value_to_string(user))
        uidb64 = urlsafe_base64_encode(user_pk_bytes)
        user_mail = user.email
        token = token_generator.make_token(user)

        current_site = get_current_site(self.context["request"])
        site_name = current_site.name
        domain = current_site.domain
        use_https = self.context["request"].is_secure()

        send_verification_mail_task.delay(
            uidb64, user_mail, token, use_https, site_name, domain
        )

        return user
