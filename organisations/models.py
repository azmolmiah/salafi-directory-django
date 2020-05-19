from django.db import models
from datetime import datetime
from django_countries.fields import CountryField

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    country = CountryField()
    description = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    mixlr = models.URLField(blank=True)
    soundcloud = models.URLField(blank=True)
    types = models.CharField(max_length=20, choices=[('Centre', 'Centre'), ('School', 'School'), ('Store', 'Store'), ('Pilgrimage', 'Pilgrimage'), ('Charity', 'Charity')])
    logo = models.ImageField(upload_to='logos/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
