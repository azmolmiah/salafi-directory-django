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
        PARAMS = {'apikey': api_key, 'q': organisation.address +
                  ',' + organisation.zipcode}

        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        latitude = data['items'][0]['position']['lat']
        longitude = data['items'][0]['position']['lng']
        lat_lng_coords = float(latitude),float(longitude)
        latlng.append(lat_lng_coords)

  context = {
    'latlng': json.dumps(latlng)
  }

  return render(request, 'maps/maps.html', context)
