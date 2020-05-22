from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Organisation


def index(request):
    organisations = Organisation.objects.all().prefetch_related('class_set')
    paginator = Paginator(organisations, 6)
    page = request.GET.get('page')
    paged_organisations = paginator.get_page(page)
    context = {
        'organisations': paged_organisations
    }
    return render(request, 'organisations/organisations.html', context)


def organisation(request, organisation_id):
    organisation = get_object_or_404(Organisation, pk=organisation_id)
    context = {
        'organisation': organisation
    }
    return render(request, 'organisations/organisation.html', context)


def search(request):
    return render(request, 'organisations/search.html')
