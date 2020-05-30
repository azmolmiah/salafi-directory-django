from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
from administrators.models import Administrator
from django.contrib.auth import get_user_model

class Organisation(models.Model):
    account = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    administrator = models.OneToOneField(Administrator, null=True, on_delete=models.CASCADE, blank=True)
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
    photo_main = models.ImageField(upload_to='photos/', default='photos/')
    photo_1 = models.ImageField(upload_to='photos/', default='photos/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/', default='photos/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/', default='photos/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/', default='photos/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/', default='photos/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
