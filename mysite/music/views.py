from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Track, YearFilter
from .serializers import TrackSerializer

# Create your views here.

class TrackViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrackSerializer

    def get_queryset(self):
        queryset = Track.objects.all().order_by('order')
        year_slug = self.request.query_params.get('year')

        if year_slug:
            queryset = queryset.filter(year__slug=year_slug)

        return queryset


def music_list(request, year_slug=None):
    # Используем глобальный год из request, если не передан явно в URL
    if not year_slug:
        year_slug = getattr(request, 'global_year_slug', '2017')

    year = get_object_or_404(YearFilter, slug=year_slug)
    musics = Track.objects.filter(year=year)

    return render(request, "music/index.html", {
        "musics": musics,
        'year': year,
        'selected_year': year_slug  # для совместимости
    })


