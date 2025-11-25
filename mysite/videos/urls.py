from django.urls import path
from .views import video_list

app_name = 'videos'

urlpatterns = [
    path('', video_list, name='videos_index'),  # отображение основной страницы videos
]