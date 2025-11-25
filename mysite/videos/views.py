from django.shortcuts import render
from .models import Video

# Create your views here.


def video_list(request, category_slug=None):
    videos = Video.objects.all()
    return render(request, "videos/index.html", {"videos": videos})










