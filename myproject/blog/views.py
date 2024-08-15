from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    contexto = {
        'nombre': 'guillermo',
        'edad': 23,
        'nacionalidad': 'chilena',
    }
    return render(request, 'index.html', contexto)