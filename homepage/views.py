from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
menu = ["Этот", "список", "вызывается", "в", "файле" ,"/homepage/views.py"]


def index(request):
    #return HttpResponse("<h1>This is HomePage!</h1>")
    return render(request, 'homepage/index.html', {'menu': menu, 'title': 'Главная страница'})

def qwerty(request):
    return HttpResponse("<h1>QWERTY!</h1>")

def qwe(request):
    #return HttpResponse("<h1>This is HomePage!</h1>")
    return render(request, 'homepage/qwe.html')

def docker(request):
    return render(request, 'homepage/docker.html')

def systemd(request):
    return render(request, 'homepage/systemd.html')

def PackageNotFoundError(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')