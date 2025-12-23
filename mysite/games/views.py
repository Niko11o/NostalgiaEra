from django.shortcuts import render, get_object_or_404
from .models import YearFilter, Games

# Create your views here.



def game_list(request, year_slug=None):
    # Используем глобальный год из request, если не передан явно в URL
    if not year_slug:
        year_slug = getattr(request, 'global_year_slug', '2017')

    year = get_object_or_404(YearFilter, slug=year_slug)
    games = Games.objects.filter(year=year)

    return render(request, "games/index.html", {
        "games": games,
        'year': year,
        'selected_year': year_slug  # для совместимости
    })


"""
def game_list(request):
    games = Games.objects.all()
    return render(request, "games/index.html", {"games": games})
"""

def games_detail(request, id, slug):
    selected = get_object_or_404(Games, id=id, slug=slug)
    return render(request, 'games/selected_games.html', {"selected": selected,})