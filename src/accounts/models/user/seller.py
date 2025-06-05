from .base import User, UserManager


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
