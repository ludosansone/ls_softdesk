from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer



class SignupSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'firstname', 'lastname', 'password1', 'password2')
