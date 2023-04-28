from rest_framework.permissions import BasePermission
from api.models import Project


class IsProjectAuthorOrContributor(BasePermission):
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
