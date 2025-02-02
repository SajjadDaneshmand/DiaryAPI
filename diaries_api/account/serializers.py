from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    diaries = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='diaries',
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'diaries')
