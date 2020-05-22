from django.db import models
from django_countries.fields import CountryField


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    country = CountryField()
    type = models.CharField(max_length=20, choices=[(
        'Student of Knowledge', 'Student of Knowledge'), ('Scholar', 'Scholar')])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
