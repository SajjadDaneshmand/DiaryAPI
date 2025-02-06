# dj
from django.urls import path, include

# rest_framework
from rest_framework.routers import DefaultRouter

# internal
from account import views


router = DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
