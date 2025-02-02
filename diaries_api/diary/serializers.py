# rest_framework
from rest_framework import serializers

# internal
from diary.models import Diary


class DiarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diary
        fields = ('owner', 'title', 'content', 'created_at')
        read_only_fields = ('created_at', )
