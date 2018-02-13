from rest_framework import permissions


class IsAdminOrSelf(permissions.BasePermission):
    """
        Verifica si usuario es administrador o si mismo.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or\
            (obj.id == request.user.id)
