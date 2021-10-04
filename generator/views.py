from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'home.html', {'password': 'tonywashere'})

def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))
    if request.GET.get('special'):
        chars.extend(list(r'!£$%^&*@~#?,.{}[]'))
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))
    length = int(request.GET.get('length'))
    pwd = ''
    for x in range(length):
        pwd += random.choice(chars)

    return render(request, 'password.html', {'password': pwd})

def about(request):
    return render(request, 'about.html')