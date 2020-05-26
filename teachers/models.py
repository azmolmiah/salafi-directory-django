from django.db import models
from django_countries.fields import CountryField
class Teacher(models.Model):
    teachers = models.ManyToManyField('self', null=True, blank=True)
    name = models.CharField(max_length=200)
    country = CountryField()
    twitter = models.URLField(blank=True)
    type = models.CharField(max_length=20, choices=[(
        'Student of Knowledge', 'Student of Knowledge'), ('Scholar', 'Scholar')])
    is_present = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
