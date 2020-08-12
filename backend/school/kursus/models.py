from django.db import models

class Students(models.Model):
  kelas_choices = (
    ('Python', 'Python'),
    ('Ruby', 'Ruby'),
    ('Vue.js', 'Vue.js'),
  )

  nama = models.CharField(max_length=100)
  kelas = models.CharField(max_length=6, choices=kelas_choices, default='Python')
  status = models.BooleanField(default=True)
  tgl_masuk = models.DateTimeField(auto_now_add=True)
  poin = models.IntegerField()

  def __str__(self):
    return self.nama
