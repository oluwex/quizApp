from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer

User = get_user_model()

class UserViewSet(CreateAPIView):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)
    