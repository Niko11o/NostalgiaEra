from django.db import models

# Create your models here.


class Track(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='tracks/')  # путь к аудиофайлу
    order = models.PositiveIntegerField(default=0)  # порядок воспроизведения, если нужно
