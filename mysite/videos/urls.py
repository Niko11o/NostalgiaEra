from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='videos_index'),  # отображение основной страницы videos
]