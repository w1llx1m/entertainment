from django.shortcuts import render
import requests as rqt
import json

def home(request):
    context = climate()
    Roundedret = round(context['current']['temperature_2m'])
    context['current']['temperature_2m'] = str(Roundedret)
    return render(request, 'home.html', context)


def climate():
    ret = rqt.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m")
    jsonret = json.loads(ret.content.decode('utf-8'))
    print(jsonret)
    return jsonret