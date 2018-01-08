from django.conf import settings
from django.conf.urls import include, url
from rest_framework import routers

from . import views
from .views import GroupViewSet, UserViewSet, SubjectViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
