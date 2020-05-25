from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django_countries import countries

from .models import Lecture
from .models import Organisation

def index(request):
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
            queryset_list = queryset_list.filter(organisation__name=organisation)

    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_lectures = paginator.get_page(page)
    context = {
        'lectures': paged_lectures,
        'orgs': orgs,
        'countries': countries,
        'values': request.GET
    }
    return render(request, 'lectures/lectures.html')
