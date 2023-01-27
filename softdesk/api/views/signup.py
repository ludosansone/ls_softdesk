from django.contrib.auth import get_user_model
from api.serializers.signup import SignupSerializer
from rest_framework.generics import CreateAPIView


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer
    queryset = get_user_model().objects.all()
