from django.shortcuts import render
from .models import YearFilter, Games

# Create your views here.


def game_list(request):
    games = Games.objects.all()
    return render(request, "games/index.html", {"games": games})