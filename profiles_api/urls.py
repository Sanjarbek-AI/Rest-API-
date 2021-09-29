from django.urls import path

from .views import HelloAPIView

app_name = 'api'

urlpatterns = [
    path('hello/', HelloAPIView.as_view(), name='hello')
]
