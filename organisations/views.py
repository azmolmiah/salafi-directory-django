from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django_countries import countries
from django.core.cache import cache

from .models import Organisation


def index(request):
    queryset_list = None

    if cache.get('cached_organisations_queryset_list'):
        queryset_list = cache.get('cached_organisations_queryset_list')
    else:
        queryset_list = Organisation.objects.order_by('-created')
        cache.set('cached_organisations_queryset_list', queryset_list, 60 * 60 * 24 * 7)
    
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(name__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Country
    if 'country' in request.GET:
        country = request.GET['country']
        if country:
            queryset_list = queryset_list.filter(country__iexact=country)

    # Type
    if 'types' in request.GET:
        types = request.GET['types']
        if types:
            queryset_list = queryset_list.filter(types__iexact=types)

    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_organisations = paginator.get_page(page)

    context = {
        'organisations': paged_organisations,
        'countries': countries,
        'values': request.GET
    }

    return render(request, 'organisations/organisations.html', context)


def organisation(request, organisation_id):
    organisation = None

    if cache.get('get_object_or_404_organisation'):
        organisation = cache.get('get_object_or_404_organisation')
    else:
        organisation = get_object_or_404(Organisation, pk=organisation_id)
        cache.set('get_object_or_404_organisation', organisation, 60 * 60 * 24 * 7)

    context = {
        'organisation': organisation
    }

    return render(request, 'organisations/organisation.html', context)
