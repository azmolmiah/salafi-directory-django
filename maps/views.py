import requests
import json
from django.shortcuts import render
from organisations.models import Organisation
from django.conf import settings
from django.core.cache import cache

def index(request):
  organisations = None

  cached_organisations = cache.get('organisations')

  if cached_organisations:
    organisations = cache.get('organisations')
  else:
    organisations = Organisation.objects.all()
    cache.set('organisations', organisations, 60 * 60 * 24 * 7)

  latlng = []

  if not latlng:
    for organisation in organisations:
      URL = "https://geocode.search.hereapi.com/v1/geocode"
      # Acquire from developer.here.com
      api_key = settings.HERE_MAPS_API_KEY
      PARAMS = {'apikey': api_key, 'q': organisation.address + ',' + organisation.city + ',' + organisation.zipcode + ',' + organisation.country.code}
      # sending get request and saving the response as response object
      r = requests.get(url=URL, params=PARAMS)
      data = r.json()
      latitude = data['items'][0]['position']['lat']
      longitude = data['items'][0]['position']['lng']
      details = {
        "lat": float(latitude),
        "lng": float(longitude),
        "name": organisation.name,
        "types": organisation.types,
        "address": organisation.address,
        "city": organisation.city,
        "zipcode": organisation.zipcode
      }
      latlng.append(dict(details))
      cache.set('data', latlng, 60 * 24 * 7)
  else:
      latlng = cache.get('data')

  context = {
    'latlng': json.dumps(latlng),
    'apiKey': settings.HERE_MAPS_API_KEY
  }

  return render(request, 'maps/maps.html', context)
