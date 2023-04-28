from rest_framework.serializers import ModelSerializer
from api.models import Issue
from api.serializers.comment import CommentListSerializer


class IssueListSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'title', 'description', 'project', 'author', 'assigned',
                  'tag', 'priority', 'status', 'created_time')


class IssueDetailSerializer(ModelSerializer):
    comments = CommentListSerializer(many=True)

    class Meta:
        model = Issue
        fields = ('id', 'title', 'description', 'project', 'comments',
                  'tag', 'priority', 'status', 'author', 'assigned', 'created_time')
