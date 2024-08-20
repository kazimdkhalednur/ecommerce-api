from rest_framework import serializers

from ..models import Buyer


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

        return user
