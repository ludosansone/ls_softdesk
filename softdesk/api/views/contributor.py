from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from api.models import Contributor
from api.serializers.contributor import ContributorListSerializer, ContributorDetailSerializer


class ContributorViewSet(ModelViewSet):
    list_serializer_class = ContributorListSerializer
    retrieve_serializer_class = ContributorDetailSerializer

    def get_queryset(self):
        return Contributor.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.retrieve_serializer_class
        return self.list_serializer_class
