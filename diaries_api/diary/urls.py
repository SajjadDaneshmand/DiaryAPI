# django
from django.urls import path, include

# rest_framework
from rest_framework.routers import DefaultRouter

# internal
from diary import views


# create a router and register views
router = DefaultRouter()
router.register(r'', views.DiaryViewSet)


urlpatterns = [
    path('', include(router.urls))
]
