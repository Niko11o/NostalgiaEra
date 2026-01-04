from django.urls import path
from .views import starter_test

app_name = 'musics'

urlpatterns = [
    path('', starter_test, name='musics_index'),

]