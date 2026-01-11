from django.urls import path, include
from .views import starter_test, TrackViewSet
from rest_framework.routers import DefaultRouter

app_name = 'musics'

router = DefaultRouter()
router.register(r'tracks', TrackViewSet, basename='tracks')

urlpatterns = [
    path('', starter_test, name='musics_index'),
    path('api/', include(router.urls))

]