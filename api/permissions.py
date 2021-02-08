from django.contrib.auth.models import Group
from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(Group.objects.get(name='SuperUser').
                        user_set.filter(id=request.user.id).exists())
        if view.action == 'list':
            return request.user.is_authenticated and request.user.is_staff
        elif view.action == 'create':
            return request.user.is_authenticated and request.user.is_staff
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False


    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if view.action == 'retrieve':
            return obj == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False