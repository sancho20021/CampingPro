"""CampingPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from App.views import index, home_page, login_page, register_page, user_cab, objects_list, logout_page, new_thing, \
    duties_list, new_duty

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index),
    path('home_page', home_page),
    path('login_page', login_page),
    path('register_page', register_page),
    path('user_cab', user_cab),
    path('objects_list/<str:type>', objects_list),
    path('logout', logout_page),
    path('new_thing', new_thing),
    path('duties_list', duties_list),
    path('new_duty', new_duty),
]
