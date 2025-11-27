from django.urls import path
from .views import video_list, video_detail

app_name = 'videos'

urlpatterns = [
    path('', video_list, name='videos_index'),  # отображение основной страницы videos

    path('<int:id>/<slug:slug>/', video_detail,
         name='video_detail'),

]