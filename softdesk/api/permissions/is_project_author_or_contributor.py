from rest_framework.permissions import BasePermission
from api.models import Project


class IsProjectAuthorOrContributor(BasePermission):
    def has_permission(self, request, view):
        """
            Renvoie True si l'utilisateur connecté est l'auteur du projet correspondants aux issues ou aux contributors
            ou s'il se trouve dans la liste des contributeurs du projet
        """

        id = view.kwargs.get('id')
        project = Project.objects.get(id=id)

        if project.author == request.user:
            return True

        contributors = project.contributors.all()

        for contributor in contributors:
            if contributor.user == request.user:
                return True

        return False
