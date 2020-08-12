from django.shortcuts import render
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import viewsets


class StudentsViewSet(viewsets.ModelViewSet):
  queryset = Students.objects.all()
  serializer_class = StudentsSerializer


def home(request):
  return render(request, 'home.html')