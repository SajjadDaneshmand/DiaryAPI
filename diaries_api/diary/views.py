# rest_framework
from rest_framework import viewsets, mixins, permissions

# internal
from diary.models import Diary
from diary.serializers import DiarySerializer
from diary.permissions import IsDiaryAccessible


class DiaryViewSet(
            mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.DestroyModelMixin,
            mixins.ListModelMixin,
            viewsets.GenericViewSet
        ):

    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsDiaryAccessible, )

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(is_public=True)
        super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
