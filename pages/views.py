from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
from classes.models import Class

def index(request):
    classes = Class.objects.all()[:3]
    context = {
        'classes': classes
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
