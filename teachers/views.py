from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django_countries import countries
from django.core.cache import cache

from .models import Teacher

def index(request):
  queryset_list = None

  if cache.get('cached_teachers_queryset_list'):
    queryset_list = cache.get('cached_teachers_queryset_list')
  else:
    queryset_list = Teacher.objects.order_by('-created')
    cache.set('cached_teachers_queryset_list', queryset_list, 60 * 60 * 24 * 7)

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(name__icontains=keywords)

  # Types
  if 'types' in request.GET:
    types = request.GET['types']
    if types:
      queryset_list = queryset_list.filter(type=types)

  # Country
  if 'country' in request.GET:
    country = request.GET['country']
    if country:
      queryset_list = queryset_list.filter(country=country)

  paginator = Paginator(queryset_list, 12)
  page = request.GET.get('page')
  paged_teachers = paginator.get_page(page)
  context = {
        'teachers': paged_teachers,
        'countries': countries,
        'values': request.GET
  }

  return render(request, 'teachers/teachers.html', context)