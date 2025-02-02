# rest_framework
from rest_framework import viewsets, mixins
from rest_framework.response import Response

# internal
from diary.models import Diary
from diary.serializers import DiarySerializer


class DiaryViewSet(
            mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.DestroyModelMixin,
            mixins.ListModelMixin,
            viewsets.GenericViewSet
        ):

    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    # permission_classes = []  # TODO: Specify permissions

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
