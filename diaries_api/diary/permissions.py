from rest_framework import permissions


class IsDiaryAccessible(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not obj.is_public and obj.owner != request.user:
            return False
        return True
