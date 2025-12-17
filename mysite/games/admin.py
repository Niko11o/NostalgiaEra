from django.contrib import admin
from .models import Games, Screenshot , YearFilter

# Register your models here.



class ScreenshotInline(admin.TabularInline):
    model = Screenshot
    extra = 5


class GamesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ScreenshotInline]


admin.site.register(Games, GamesAdmin)

class YearFilterAdmin(admin.ModelAdmin):
    list_display = ['year', 'slug']
    prepopulated_fields = {'slug': ('year',)} # Слаг заполняется в соответствии с названием товара

admin.site.register(YearFilter, YearFilterAdmin)
