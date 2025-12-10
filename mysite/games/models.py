from django.db import models
from django.urls import reverse


# Create your models here.

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
        return reverse('###:product_list_by_year', args=[self.slug])



class Games(models.Model):
    year = models.ForeignKey(YearFilter, db_index=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    genre = models.CharField(max_length=50, db_index=True)
    description = models.CharField()
    date = models.DateTimeField()
    slug = models.SlugField(max_length=100, unique=100)
    torrent_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Добавление игры'

    def get_absolute_url(self):
        return reverse('games:###', args=[self.id, self.slug])