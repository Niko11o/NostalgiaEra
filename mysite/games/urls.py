from django.urls import path
from .views import starter

app_name = 'games'

urlpatterns = [
    path('', starter, name='games_index'),

]
