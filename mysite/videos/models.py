from django.db import models
from django.urls import reverse


class Video(models.Model):
    name = models.CharField(max_length=40, db_index=True)
    chanel = models.CharField(max_length=40, db_index=True)
    date = models.DateTimeField()
    preview = models.ImageField(upload_to='video_previev/', blank=True)
    slug = models.SlugField(max_length=100, unique=100)
    redirect = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Добавление видео'

    def get_absolute_url(self):
        return reverse('videos:video_detail', args=[self.id, self.slug])