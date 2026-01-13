from django.urls import path, include
from .views import music_list, TrackViewSet
from rest_framework.routers import DefaultRouter

app_name = 'musics'

router = DefaultRouter()
router.register(r'tracks', TrackViewSet, basename='tracks')

urlpatterns = [
    path('', music_list, name='musics_index'),
    path('api/', include(router.urls)),
    path('<slug:year_slug>/', music_list,
         name='product_list_by_year'),

]