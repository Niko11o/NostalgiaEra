from django.shortcuts import render, get_object_or_404
from .models import Video

# Create your views here.


def video_list(request):
    videos = Video.objects.all()
    return render(request, "videos/index.html", {"videos": videos})



def video_detail(request, id, slug):
    selected = get_object_or_404(Video, id=id, slug=slug)

    return render(request, 'videos/selected_video.html', {'selected': selected})







