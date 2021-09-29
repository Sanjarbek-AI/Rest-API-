from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import HelloAPIView, HelloViewset, UserProfileViewset

router = DefaultRouter()
router.register('hello-viewset', HelloViewset, basename='hello-viewset')
router.register('profile', UserProfileViewset)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
