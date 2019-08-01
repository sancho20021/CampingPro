from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import Thing


def index(request):
    return HttpResponse("Это пустая страница!")


def new_thing(request):
    if request.method == 'GET':
        return render(request, 'new_thing.html')
    if request.method == 'POST':
        thing = Thing()
        name = request.POST.get('name', '')
        type = request.POST.get('type', '')
        price = request.POST.get('price', 0)
        kol = request.POST.get('kol', 1)
        if name == '' or type == '':
            return HttpResponse("Заполните все поля!")
        thing.name = name
        thing.type = type
        thing.price = price
        thing.kol = kol
        thing.save()
        return redirect('/objects_list/'+thing.type)


def home_page(request):
    users = User.objects.all()
    return render(request, 'home_page.html', {'users': users})


def objects_list(request, type):
    if request.user.is_authenticated:
        things = Thing.objects.filter(type=type)
        return render(request, 'objects_list.html', {'things': things, 'type': type})
    else:
        redirect('/login_page')


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
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')

        if username == '' or password == '' or first_name == '' and last_name == '':
            return HttpResponse("Введите все поля")
        if User.objects.filter(username=username).exists():
            return HttpResponse("Логин занят")
        user = User.objects.create_user(username, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        login(request, user)
        return redirect('/user_cab')


def logout_page(request):
    logout(request)
    return redirect('/home_page')
