from django.http.response import BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse
from .settings import BASE_DIR
import os



def home(request):
    #return HttpResponse("<h1> Hello world </h1>")
    return render(request, 'index.html')


def games(request):
    return render(request, 'games.html')


def assets(request):
    #return HttpResponse("<h1> Hello world </h1>")
    return render(request, 'assets.html')


def meeting(request):
    return render(request, 'meeting.html')


def nfts(request):
    #return HttpResponse("<h1> Hello world </h1>")
    return render(request, 'nfts.html')


