from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
class Organisation(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    country = CountryField()
    description = models.TextField(blank=True)
    types = models.CharField(max_length=20, choices=[('Centre','Centre'), ('School','School'),('Store','Store'),('Pilgrimage','Pilgrimage'),('Charity','Charity')])
    logo = models.ImageField(upload_to='logos/')
    creation_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name
