from rest_framework.permissions import BasePermission

class PermisosPersonalizados(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user.TieneRol("SUPER ADMIN") or obj.Id == request.user.Id)