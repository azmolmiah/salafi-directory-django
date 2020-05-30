from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
from django_countries import countries
from classes.models import Class
from lectures.models import Lecture
from organisations.models import Organisation

def index(request):
    ip = request.META.get('REMOTE_ADDR')
    g = GeoIP2('GeoLite2-Country_20200519')
    country_code = g.country_code('15.194.1.177')
    country_name = g.country_name('15.194.1.177')
    organisation = Organisation.objects.filter(country='GB')
    classes = Class.objects.all().filter(organisation__in=organisation).order_by('-created')[:3]
    lectures = Lecture.objects.all().filter(organisation__in=organisation).order_by('-created')[:3]
    context = {
        'classes': classes,
        'lectures': lectures,
        'country_name': country_name,
        'countries': countries
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
