from django.shortcuts import render
from rest_framework import viewsets
from .models import Track
from .serializers import TrackSerializer

# Create your views here.

class TrackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  Track.objects.all().order_by('order')
    serializer_class = TrackSerializer


def starter_test(request):
    return render(request, 'music/index.html', )


