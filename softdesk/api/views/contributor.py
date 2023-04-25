from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Contributor
from api.serializers.contributor import ContributorListSerializer, ContributorDetailSerializer


class ContributorViewSet(ModelViewSet, CreateModelMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    list_serializer = ContributorListSerializer
    retrieve_serializer = ContributorDetailSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Contributor.objects.filter(project__id=id)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.retrieve_serializer
        return self.list_serializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
