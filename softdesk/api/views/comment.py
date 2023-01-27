from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.models import Comment
from api.serializers.comment import CommentListSerializer, CommentDetailSerializer


class CommentViewSet(ModelViewSet):
    list_serializer_class = CommentListSerializer
    retrieve_serializer_class = CommentDetailSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.retrieve_serializer_class
        return self.list_serializer_class
