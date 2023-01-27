from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.models import Contributor


class ContributorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('id', 'role', 'user', 'project')


class ContributorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('id', 'role', 'permission', 'user', 'project')
