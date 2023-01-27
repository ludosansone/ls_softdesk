from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class SignupSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
