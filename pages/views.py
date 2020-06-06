from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
from django_countries import countries
from classes.models import Class
from lectures.models import Lecture
from organisations.models import Organisation

def index(request):
    ip = request.META.get('REMOTE_ADDR')
    g = GeoIP2('GeoLite2-Country_20200519')
    g_city = GeoIP2('GeoLite2-City_20200602')
    country_code = g.country_code('185.35.50.4')
    country_name = g.country_name('185.35.50.4')
    time_zone = g_city.city('185.35.50.4')['time_zone']
    organisation = Organisation.objects.filter(country=country_code)
    classes = Class.objects.all().filter(organisation__in=organisation).order_by('-created')[:3]
    lectures = Lecture.objects.all().filter(organisation__in=organisation).order_by('-created')[:3]
    context = {
        'classes': classes,
        'lectures': lectures,
        'country_name': country_name,
        'countries': countries,
        'time_zone': time_zone
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
