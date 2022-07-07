from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.permissions import AllowAny


class IsAuthorOrReadOnlyOrModeratorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return (request.user in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.user == obj.author
                or request.user.is_moderator
                or request.user.is_admin)


class DetailForAdmin(BasePermission):
    def has_permission(self, request, view):
        return (request.user in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return request.user.is_admin


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated
                and (request.user.is_staff
                     or request.user.is_admin))


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.is_admin)


class OwnProfilePermission(BasePermission):

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return (AllowAny(),)
        return (IsAuthorOrReadOnlyOrModeratorOrAdmin(),)
