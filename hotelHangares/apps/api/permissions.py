from rest_framework.permissions import BasePermission


class IsReceptionist(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.tipoUsuario.id is 2


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.tipoUsuario.id is 3


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # print(request.user.tipoUsuario.id is 1)
        return request.user and request.user.tipoUsuario.id is 1
