from api.models import Comment
from rest_framework.serializers import ModelSerializer


class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'description', 'issue')

class CommentDetailSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'description', 'created_time', 'issue', 'author')
