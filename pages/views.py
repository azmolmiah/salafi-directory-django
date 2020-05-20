from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
from classes.models import Class
from organisations.models import Organisation

def index(request):
    g = GeoIP2('GeoLite2-Country_20200519')
    country_code = g.country_code('15.194.1.177')
    organisations = Organisation.objects.filter(country=f'{country_code}')
    classes = Class.objects.all().filter(organisation__in=organisations).order_by('-created')[:3]
    context = {
        'classes': classes
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
