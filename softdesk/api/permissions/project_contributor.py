from rest_framework.permissions import BasePermission


class IsContributor(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True

        contributors = obj.contributors.all()

        for contributor in contributors:
            if contributor.user == request.user:
                return True

        return False
