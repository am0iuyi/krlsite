from django.shortcuts import render
from .models import Article

def home(request):
    return render(request, 'home.html')

def game(request):  # Эта функция должна быть определена
    articles = Article.objects.all()
    return render(request, 'game.html', {'articles': articles})

def facts(request):  # Эта функция должна быть определена
    articles = Article.objects.all()
    return render(request, 'facts.html', {'articles': articles})

def thoto(request):  # Эта функция должна быть определена
    articles = Article.objects.all()
    return render(request, 'thoto.html', {'articles': articles})


def history(request):  # Эта функция должна быть определена
    articles = Article.objects.all()
    return render(request, 'history.html', {'articles': articles})

def love(request):  # Эта функция должна быть определена
    articles = Article.objects.all()
    return render(request, 'love.html', {'articles': articles})