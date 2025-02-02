# django
from django.contrib.auth.models import User

# rest_framework
from rest_framework import viewsets

# internal
from account.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
