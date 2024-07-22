from django.shortcuts import render
import requests as rqt
import json

def home(request):
    context = {}
    return render(request, 'home.html', context)
