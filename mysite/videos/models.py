from django.db import models
from django.urls import reverse

class YearFilter(models.Model):
    year = models.CharField(max_length=100, db_index=True, verbose_name='Год', null=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('year',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.year

    def get_absolute_url(self):
        return reverse('videos:product_list_by_year', args=[self.slug])


class Video(models.Model):
    year = models.ForeignKey(YearFilter, related_name='products', on_delete=models.CASCADE, null=True)
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