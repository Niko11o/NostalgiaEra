from django.db import models
from django.urls import reverse

# Create your models here.


class YearFilter(models.Model):
    year = models.CharField(max_length=100, db_index=True, verbose_name='Год', null=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('year',)
        verbose_name = 'Год'
        verbose_name_plural = 'Года'

    def __str__(self):
        return self.year

    def get_absolute_url(self):
        return reverse('musics:product_list_by_year', args=[self.slug])


class Track(models.Model):
    year = models.ForeignKey(YearFilter, related_name='products', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='tracks/')  # путь к аудиофайлу
    order = models.PositiveIntegerField(default=0, blank=True)  # порядок воспроизведения, если нужно
