# rest_framework
from rest_framework import serializers

# internal
from diary.models import Diary


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('id', 'owner', 'title', 'content', 'created_at', 'is_public')
        extra_kwargs = {
            "is_public": {"write_only": True},
            "owner": {"read_only": True}
        }

