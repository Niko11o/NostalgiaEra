from django.contrib import admin
from .models import Video, YearFilter

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # Слаг заполняется в соответствии с названием товара

admin.site.register(Video, VideoAdmin)

class YearFilterAdmin(admin.ModelAdmin):
    list_display = ['year', 'slug']
    prepopulated_fields = {'slug': ('year',)} # Слаг заполняется в соответствии с названием товара

admin.site.register(YearFilter, YearFilterAdmin)