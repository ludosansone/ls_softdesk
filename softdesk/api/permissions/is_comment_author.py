from rest_framework.permissions import BasePermission


class IsCommentAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
            Si la requète vise à modifier ou effacer le commentaire
            renvoie True si l'utilisateur connecté est l'auteur du commentaire
        """

        if request.method in ['PUT', 'PATCH', 'DELETE']:
            if obj.author == request.user:
                return True

            return False
        return True
