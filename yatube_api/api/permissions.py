from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверяем владельца объекта"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class ReadOnly(permissions.BasePermission):
    """Запрещаем редактирование модели"""
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS