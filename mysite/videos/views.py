from django.shortcuts import render, get_object_or_404
from .models import Video, YearFilter


def video_list(request, year_slug=None):
    # Используем глобальный год из request, если не передан явно в URL
    if not year_slug:
        year_slug = getattr(request, 'global_year_slug', '2017')

    year = get_object_or_404(YearFilter, slug=year_slug)
    videos = Video.objects.filter(year=year)

    return render(request, "videos/index.html", {
        "videos": videos,
        'year': year,
        'selected_year': year_slug  # для совместимости
    })


def video_detail(request, id, slug):
    selected = get_object_or_404(Video, id=id, slug=slug)

    # Фильтруем связанные видео по глобальному году
    global_year_slug = getattr(request, 'global_year_slug', '2017')
    related_videos = Video.objects.filter(
        year__slug=global_year_slug
    ).exclude(id=selected.id)[:4]

    return render(request, 'videos/selected_video.html', {
        'selected': selected,
        'related_videos': related_videos
    })



