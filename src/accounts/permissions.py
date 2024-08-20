from rest_framework.permissions import IsAuthenticated


class IsBuyer(IsAuthenticated):
    """
    Allows access only to buyer users.
    """

    def has_permission(self, request, view):
        return bool(request.user.is_buyer and super().has_permission(request, view))


class IsSeller(IsAuthenticated):
    """
    Allows access only to seller users.
    """

    def has_permission(self, request, view):
        return bool(request.user.is_seller and super().has_permission(request, view))
