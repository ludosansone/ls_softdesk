from rest_framework.permissions import BasePermission


class IsAuthorOrContributor(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
            Renvoie True si l'utilisateur connecté est l'auteur du projet
            ou s'il se trouve dans la liste des contributeurs du projet
        """

        if obj.author == request.user:
            return True

        contributors = obj.contributors.all()

        for contributor in contributors:
            if contributor.user == request.user:
                return True
        return False
