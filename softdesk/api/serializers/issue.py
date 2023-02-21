from api.models import Issue
from rest_framework.serializers import ModelSerializer


class IssueListSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'title', 'description', 'project',
                  'tag', 'priority', 'status', 'author', 'assigned', 'created_time')


class IssueDetailSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'title', 'description', 'project',
                  'tag', 'priority', 'status', 'author', 'assigned', 'created_time')
