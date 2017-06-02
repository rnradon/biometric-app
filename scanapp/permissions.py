from rest_framework.permissions import BasePermission, SAFE_METHODS
# from rest_framework import permissions

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user


# from rest_framework import permissions

# class IsAuthenticated(permissions.IsAuthenticated):
#     def has_permission(self, request, view):
#         if request.method == 'POST':
#             return True
#         return super(IsAuthenticatedOrCreate, self).has_permission(request, view)