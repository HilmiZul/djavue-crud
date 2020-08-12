from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from kursus.views import StudentsViewSet, home

router = routers.DefaultRouter()
router.register('students', StudentsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home),
]
