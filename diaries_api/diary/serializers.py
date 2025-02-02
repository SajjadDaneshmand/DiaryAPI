from rest_framework import serializers

from diary.models import Diary


class DiarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diary
        fields = ('owner.username', 'title', 'content', 'created_at')
        read_only_fields = ('created_at', )
