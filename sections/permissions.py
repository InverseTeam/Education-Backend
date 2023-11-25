from rest_framework import permissions


class IsSectionAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.role.role_type == 'teacher' and request.user == obj.author
    

class IsSectionAuthorOrTeacherOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.role.role_type == 'teacher' and (request.user == obj.author or
                                                             False not in [request.user == group.teacher for group in obj.groups])

