from django.shortcuts import render
from django.http import HttpResponse
from mytest.models import GameKind

# Create your views here.

def index(request):

    hot_game = GameKind.objects.filter(kind__name='流行')
    new_game = GameKind.objects.filter(kind__name='最新')
    recommend_game = GameKind.objects.filter(kind__name='编辑推荐')
    data = GameKind.objects.all().order_by('-id')

    return render(request, 'index.html', {'games': data,
                                          'hg': hot_game,
                                          'ng': new_game,
                                          'rg': recommend_game,
                                          })

