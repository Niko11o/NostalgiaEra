from django.urls import path
from .views import game_list

app_name = 'games'

urlpatterns = [
    path('', game_list, name='games_index'),

]
