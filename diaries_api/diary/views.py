# dj
from django.db.models import Q

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

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(Q(is_public=True) | Q(owner=self.request.user))
        return queryset.filter(is_public=True)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
