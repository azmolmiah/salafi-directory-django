import requests
import json
from django.shortcuts import render

from organisations.models import Organisation


def index(request):
  organisations = Organisation.objects.all()

  latlng = []

  for organisation in organisations:
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    # Acquire from developer.here.com
    api_key = 'LNGJKlqzncGWlpgjAy0svm4OGEl0FdN2Cpk_XJrQOQs'
    PARAMS = {'apikey': api_key, 'q': organisation.address + ',' + organisation.city + ',' + organisation.zipcode}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']
    details = {
      "lat": float(latitude),
      "lng": float(longitude),
      "name": organisation.name,
      "address": organisation.address,
      "city": organisation.city,
      "zipcode": organisation.zipcode
    }
    latlng.append(dict(details))
  
  context = {
    'latlng': json.dumps(latlng)
  }

  return render(request, 'maps/maps.html', context)