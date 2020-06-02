from django.shortcuts import render
from organisations.models import Organisation

def index(request):
  organistion = Organisation.objects.filter(types='Centre')
  context = {
    'org': organistion,
  }
  return render(request, 'maps/maps.html')