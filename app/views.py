from django.http import HttpResponse
from django.shortcuts import render, reverse

import datetime
import os

path = '.'

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = "app/current_time.html"
    current_time = datetime.datetime.now().time()
    format = ''
    msg = f'{current_time.strftime("%H:%M:%S")}'
    context = {
        'time_current': msg
    }
    return render(request, template_name, context)

def workdir_view(request):
    list_dir = sorted(os.listdir(path))
    template_name = "app/work_dir.html"
    context = {
        'list': list_dir
    }

    return render(request, template_name, context)