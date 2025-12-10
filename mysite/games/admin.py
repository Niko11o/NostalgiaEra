from django.contrib import admin
from .models import Games, YearFilter

# Register your models here.



class GamesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Games, GamesAdmin)

class YearFilterAdmin(admin.ModelAdmin):
    list_display = ['year', 'slug']
    prepopulated_fields = {'slug': ('year',)} # Слаг заполняется в соответствии с названием товара

admin.site.register(YearFilter, YearFilterAdmin)
