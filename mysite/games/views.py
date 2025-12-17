from django.shortcuts import render, get_object_or_404
from .models import YearFilter, Games

# Create your views here.


def game_list(request):
    games = Games.objects.all()
    return render(request, "games/index.html", {"games": games})


def games_detail(request, id, slug):
    selected = get_object_or_404(Games, id=id, slug=slug)
    return render(request, 'games/selected_games.html', {"selected": selected,})