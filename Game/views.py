from django.shortcuts import render
from django.http import HttpResponse
from .models import *#importujemy models z projektu Game
# Create your views here.

def index(request): #stworzenie funkcji
    categories = Category.objects.all().order_by('name')
    games = Games.objects.all().order_by('name')
    platform = Platform.objects.all()
    date = {'category': categories,
            'games': games,
            'platform': platform}
    return render(request, 'home.html', date)


def category(request, id):
    category_user = Category.objects.get(pk = id)
    category_game = Games.objects.filter(category = category_user).order_by('name')
    category =  Category.objects.all().order_by('name')
    platform =  Platform.objects.all()
    date = {'category_user': category_user,
            'category_game': category_game,
            'category' : category,
            'platform' : platform}
    return render(request, 'category_game.html', date)

def game(request, id):
    game_user = Games.objects.get(pk = id)
    categories = Category.objects.all()
    platforms = Platform.objects.all()
    date = {'game_user' : game_user,
            'category': categories,
            'platform': platforms}
    return render(request, 'game.html', date)

def platform(request, id):
    platform_user = Platform.objects.get(pk = id)
    platform_game = Games.objects.filter(platform = platform_user).order_by('name')
    platform =  Platform.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')
    date = {'platform_user': platform_user,
            'platform_game': platform_game,
            'platform' : platform,
            'category': categories}
    return render(request, 'platform_game.html', date)