from django.shortcuts import render
from django.http import HttpResponse
from mytest.models import GameKind, GameVideo

# Create your views here.

def index(request):

    hot_game = GameKind.objects.filter(kind__name='流行')
    new_game = GameKind.objects.filter(kind__name='最新')
    recommend_game = GameKind.objects.filter(kind__name='编辑推荐')
    data = GameKind.objects.all().order_by('-id')
    game_video = GameVideo.objects.filter()

    return render(request, 'index.html', {'games': data,
                                          'hg': hot_game,
                                          'ng': new_game,
                                          'rg': recommend_game,
                                          'gv': game_video,
                                          })

def contact(request):
    return render(request, 'contact.html')

def game_review(request):
    return render(request, 'game-review.html')

def post(request):
    return render(request, 'post.html')

def single_game_review(request):
    return render(request, 'single-game-review.html')

def single_post(request):
    return render(request, 'single-post.html')