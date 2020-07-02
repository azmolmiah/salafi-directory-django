from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.gis.geoip2 import GeoIP2
from datetime import datetime
from django_countries import countries
from django.core.cache import cache

from .models import Class
from .models import Organisation


def index(request):
    ip = request.META.get('REMOTE_ADDR')
    g = GeoIP2('GeoLite2-City_20200602')
    time_zone = g.city(f'{ip}')['time_zone']
    queryset_list = None
    orgs = None

    if cache.get('cached_classes_queryset_list'):
        queryset_list = cache.get('cached_classes_queryset_list')
    else:
        queryset_list = Class.objects.order_by('-created')
        cache.set('cached_classes_queryset_list', queryset_list, 60 * 60 * 24)
    
    if cache.get('cached_classes_orgs'):
        orgs = cache.get('cached_classes_orgs')
    else:
        orgs = Organisation.objects.filter(types='Centre')
        cache.set('cached_classes_orgs', orgs, 60 * 60 * 24)

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(title__icontains=keywords)

    # Language
    if 'language' in request.GET:
        language = request.GET['language']
        if language:
            queryset_list = queryset_list.filter(language__iexact=language)

    # Types
    if 'types' in request.GET:
        types = request.GET['types']
        if types == 'True':
            queryset_list = queryset_list.filter(is_online=True)
        elif types == 'False':
            queryset_list = queryset_list.filter(is_online=False)

    # Country
    if 'country' in request.GET:
        country = request.GET['country']
        if country:
            queryset_list = queryset_list.filter(organisation__country=country)

    # organisations
    if 'organisation' in request.GET:
        organisation = request.GET['organisation']
        if organisation:
            queryset_list = queryset_list.filter(
                organisation__name=organisation)
    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_classes = paginator.get_page(page)
    context = {
        'classes': paged_classes,
        'orgs': orgs,
        'countries': countries,
        'values': request.GET,
        'time_zone': time_zone
    }
    return render(request, 'classes/classes.html', context)
