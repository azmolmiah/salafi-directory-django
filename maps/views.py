import requests
import json
from django.shortcuts import render
from organisations.models import Organisation
from django.conf import settings

def index(request):
  organisations = Organisation.objects.all()
  latlng = []

  if 'data' not in request.session:
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
      request.session['data'] = latlng
      request.session.set_expiry(60 * 60 * 24 * 5)
  else:
      latlng = request.session['data']

  context = {
    'latlng': json.dumps(latlng)
  }

  return render(request, 'maps/maps.html', context)
