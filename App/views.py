from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import Thing, Duty


def index(request):
    return HttpResponse("Это пустая страница!")

def duties_list(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            is_moder = False
            if request.user.groups.filter(name='moders').exists():
                is_moder = True
            duties = Duty.objects.all()
            return render(request, 'duties_list.html', {'duties': duties, 'is_moder': is_moder})
        if request.method == 'POST':
            if 'take' in request.POST:
                duty = Duty.objects.get(pk=request.POST['duty_id'])
                duty.keeper = request.user
                duty.save()
            if 'remove' in request.POST:
                duty = Duty.objects.get(pk=request.POST['duty_id'])
                duty.keeper = None
                duty.save()
            return redirect(request.path_info)
    else:
        redirect('/login_page')

def new_duty(request):
    if request.method == 'GET':
        return render(request, 'new_duty.html')
    if request.method == 'POST':
        duty = Duty()
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        if name == '':
            return HttpResponse("Заполните все поля!")
        duty.name = name
        duty.description=description
        duty.save()
        return redirect(request.path_info)

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
        return redirect(request.path_info)


def home_page(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            is_moder = False
            if request.user.groups.filter(name='moders').exists():
                is_moder = True
            users = User.objects.all()
            things = Thing.objects.filter(keeper=None)
            return render(request, 'home_page.html', {'users': users, 'things': things, 'is_moder': is_moder})
        if request.method == 'POST':
            user = User.objects.get(pk=request.POST.get('user_id'))
            thing = Thing.objects.get(pk=request.POST.get('thing_id'))
            thing.keeper = user
            thing.save()
            return redirect(request.path_info)

    else:
        return redirect('/login_page')


def objects_list(request, type):
    if request.user.is_authenticated:
        if request.method == 'GET':
            is_moder = False
            if request.user.groups.filter(name='moders').exists():
                is_moder = True
            things = Thing.objects.filter(type=type)
            return render(request, 'objects_list.html', {'things': things, 'type': type, 'is_moder': is_moder})
        if request.method == 'POST':
            if 'take' in request.POST:
                thing = Thing.objects.get(pk=request.POST['thing_id'])
                thing.keeper = request.user
                thing.save()
            if 'remove' in request.POST:
                thing = Thing.objects.get(pk=request.POST['thing_id'])
                thing.keeper = None
                thing.save()
            return redirect(request.path_info)
    else:
        redirect('/login_page')


def user_cab(request):
    things = Thing.objects.filter(keeper=request.user)
    duties = Duty.objects.filter(keeper=request.user)
    return render(request, 'user_cab.html', {'things': things, 'duties': duties})


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
        password = request.POST.get('password', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')

        if username == '' or password == '' or first_name == '' and last_name == '':
            return HttpResponse("Введите все поля")
        if User.objects.filter(username=username).exists():
            return HttpResponse("Логин занят")
        user = User.objects.create_user(username, None, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        login(request, user)
        return redirect('/user_cab')


def logout_page(request):
    logout(request)
    return redirect('/login_page')
