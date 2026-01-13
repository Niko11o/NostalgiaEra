from django.contrib import admin
from .models import Track, YearFilter

# Register your models here.


admin.site.register(Track)


class YearFilterAdmin(admin.ModelAdmin):
    list_display = ['year', 'slug']
    prepopulated_fields = {'slug': ('year',)} # Слаг заполняется в соответствии с названием товара

admin.site.register(YearFilter, YearFilterAdmin)






