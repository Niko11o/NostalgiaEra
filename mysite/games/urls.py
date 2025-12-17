from django.urls import path
from .views import game_list, games_detail

app_name = 'games'

urlpatterns = [
    path('', game_list, name='games_index'),
    path('<int:id>/<slug:slug>',games_detail, name="games_detail"),

]
