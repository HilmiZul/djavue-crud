from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Students
    fields = ['id', 'nama', 'kelas', 'status', 'tgl_masuk', 'poin']