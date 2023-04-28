from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Comment
from api.serializers.comment import CommentListSerializer, CommentDetailSerializer
from api.permissions.is_project_author_or_contributor import IsProjectAuthorOrContributor
from api.permissions.is_comment_author import IsCommentAuthor


class CommentViewSet(ModelViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticated, IsProjectAuthorOrContributor, IsCommentAuthor]
    list_serializer = CommentListSerializer
    retrieve_serializer = CommentDetailSerializer

    def get_queryset(self):
        issue_id = self.kwargs['issue_id']
        return Comment.objects.filter(issue__id=issue_id)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.retrieve_serializer
        return self.list_serializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
