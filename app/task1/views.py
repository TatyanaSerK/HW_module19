from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Buyer, Game
from .UserRegister import UserRegister
# Create your views here.

def in_platform(request):
    return render(request, 'platform.html')

def in_games(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'games.html', context)

def in_cart(request):
    return render(request, 'cart.html')


def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {'error': ['Пароли не совпадают','Вы должны быть старше 18',f'Пользователь уже существует']}
    context = {
        'users': users,
        'info': info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        error_list = info['error']
        for user in users:
            if user.name == username:
                return HttpResponse(f'{error_list[2]}')
            if int(age) < int(18):
                return HttpResponse(f'{error_list[1]}')
            if repeat_password != password:
                return HttpResponse(f'{error_list[0]}')
        Buyer.objects.create(name=username, age=age, balance=0)
        return render(request, 'platform.html')

    return render(request, 'registration_page.html', context)

