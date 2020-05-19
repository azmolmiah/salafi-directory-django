from django.shortcuts import render

from .models import Organisation

def index(request):
    organisations = Organisation.objects.all().prefetch_related('class_set')
    context = {
        'organisations' : organisations
    }
    return render(request, 'organisations/organisations.html', context)

def organisation(request, organisation_id):
    return render(request, 'organisations/organisation.html')

def search(request):
    return render(request, 'organisations/search.html')