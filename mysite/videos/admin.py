from django.contrib import admin
from .models import Video

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # Слаг заполняется в соответствии с названием товара

admin.site.register(Video, VideoAdmin)