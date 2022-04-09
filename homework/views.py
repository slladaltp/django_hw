from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello World!')

def home(request):
    container = 'Hello World!'
    return render(request, 'home.html', context={
        'container': container,
    })
