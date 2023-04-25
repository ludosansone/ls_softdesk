from rest_framework.permissions import BasePermission
from api.models import Project


class IsAuthorOrContributor(BasePermission):
    def has_permission(self, request, view):
        id = view.kwargs.get('id')
        project = Project.objects.get(id=id)

        if project.author == request.user:
            return True

        contributors = project.contributors.all()

        for contributor in contributors:
            if contributor.user == request.user:
                return True

        return False

    def has_object_permission(self, request, view, obj):
        if obj.project.author == request.user:
            return True

        contributors = obj.project.contributors.all()

        for contributor in contributors:
            if contributor.user == request.user:
                return True

        return False
