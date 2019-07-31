from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("Это пустая страница!")


def home_page(request):
    return render(request, 'home_page.html')


def user_cab(request):
    return render(request, 'user_cab.html')


def login_page(request):
    if request.method == 'GET':
        return render(request, 'login_page.html')
    if request.method == 'POST':
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            return HttpResponse("Заполните все поля")

        # проверяем правильность логина и пароля
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/user_cab')
        else:
            return HttpResponse("Логин или пароль неверен")


def register_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/user_cab')
        return render(request, 'register_page.html')
    if request.method == 'POST':
        username = request.POST.get('login', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if username == '' or email == '' or password == '':
            return HttpResponse("Введите все поля")
        if User.objects.filter(username=username).exists():
            return HttpResponse("Логин занят")
        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return redirect('/user_cab')


def logout_page(request):
    logout(request)
    return redirect('/home_page')
