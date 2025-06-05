from .base import User, UserManager


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
