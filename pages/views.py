from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
from django_countries import countries
from django.core.cache import cache

from classes.models import Class
from lectures.models import Lecture
from organisations.models import Organisation
from pages.models import Page

def index(request):
    ip = request.META.get('REMOTE_ADDR')
    g = GeoIP2('GeoLite2-City_20200602')
    country_code = g.country_code('185.35.50.4')
    country_name = g.country_name('185.35.50.4')
    time_zone = g.city('185.35.50.4')['time_zone']
    organisation = None
    classes = None
    lectures = None

    if cache.get('cached_home_organisation'):
        organisation = cache.get('cached_home_organisation')
    else:
        organisation = Organisation.objects.filter(country=country_code)
        cache.set('cached_home_organisation', organisation, 60 * 60 * 3)
    
    if cache.get('cached_home_classes'):
        classes = cache.get('cached_home_classes')
    else:
        classes = Class.objects.all().filter(organisation__in=organisation).order_by('-created')[:3]
        cache.set('cached_home_classes', classes, 60 * 60 * 3)
    
    if cache.get('cached_home_lectures'):
        lectures = cache.get('cached_home_lectures')
    else:
        lectures = Lecture.objects.all().filter(organisation__in=organisation).order_by('-created')[:3]
        cache.set('cached_home_lectures', lectures, 60 * 60 * 3)

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

def privacy(request):
    pages = None
    if cache.get('privacy'):
         pages = cache.get('privacy')
    else:
        pages = Page.objects.all().filter(slug='privacypolicy')
        cache.set('privacy', pages, 60 * 60 * 24 * 7)
    context = {
        'pages': pages,
    }
    return render(request, 'pages/privacy.html', context)

def cookies(request):
    pages = None
    if cache.get('cookies'):
         pages = cache.get('cookies')
    else:
        pages = Page.objects.all().filter(slug='cookiesandcahespolicy')
        cache.set('cookies', pages, 60 * 60 * 24 * 7)
    context = {
        'pages': pages,
    }
    return render(request, 'pages/cookies.html', context)

def conditions(request):
    if cache.get('conditions'):
         pages = cache.get('conditions')
    else:
        pages = Page.objects.all().filter(slug='conditionsofuse')
        cache.set('conditions', pages, 60 * 60 * 24 * 7)
    context = {
        'pages': pages,
    }
    return render(request, 'pages/conditions.html', context)

def qanda(request):
    if cache.get('qanda'):
         pages = cache.get('qanda')
    else:
        pages = Page.objects.all().filter(slug='questionsandaswers')
        cache.set('qanda', pages, 60 * 60 * 24 * 7)
    context = {
        'pages': pages,
    }
    return render(request, 'pages/qanda.html', context)