from uuid import uuid4

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AbstracUserManager
from django.db import models


class UserManager(AbstracUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    class UserRole(models.TextChoices):
        BUYER = "BUYER", "Buyer"
        SELLER = "SELLER", "Seller"

    id = models.UUIDField(primary_key=True, serialize=False, editable=False)
    username = None
    email = models.EmailField("Email address", unique=True)
    role = models.CharField(max_length=10, choices=UserRole.choices, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid4()
        super(User, self).save(*args, **kwargs)

    @staticmethod
    def is_buyer(self):
        return self.role == User.UserRole.BUYER


class BuyerManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role=User.UserRole.BUYER)


class Buyer(User):
    objects = BuyerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = User.UserRole.BUYER
        super(Buyer, self).save(*args, **kwargs)


class SellerManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role=User.UserRole.SELLER)


class Seller(User):
    objects = SellerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = User.UserRole.SELLER
        super(Seller, self).save(*args, **kwargs)
