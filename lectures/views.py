from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.gis.geoip2 import GeoIP2
from django_countries import countries

from .models import Lecture
from .models import Organisation


def index(request):
    ip = request.META.get('REMOTE_ADDR')
    g = GeoIP2('GeoLite2-City_20200602')
    time_zone = g.city('185.35.50.4')['time_zone']
    queryset_list = Lecture.objects.order_by('-created')
    orgs = Organisation.objects.filter(types='Centre')

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

    # Exact date
    if 'date' in request.GET:
        date = request.GET['date']
        if date:
            queryset_list = queryset_list.filter(date__iexact=date)

    # Date range
    if 'start_date' in request.GET:
        if 'end_date' in request.GET:
            start_date = request.GET['start_date']
            end_date = request.GET['end_date']
            if start_date:
                if end_date:
                    queryset_list = queryset_list.filter(
                        date__gte=start_date, date__lte=end_date)

    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_lectures = paginator.get_page(page)
    context = {
        'lectures': paged_lectures,
        'orgs': orgs,
        'countries': countries,
        'values': request.GET,
        'time_zone': time_zone
    }
    return render(request, 'lectures/lectures.html', context)
