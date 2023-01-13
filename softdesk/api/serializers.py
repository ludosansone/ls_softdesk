from api.models import Project
from rest_framework.serializers import ModelSerializer


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description')
