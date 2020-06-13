from django.db import models
from datetime import datetime
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError

class Organisation(models.Model):
    account = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    country = CountryField()
    description = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    mixlr = models.URLField(blank=True)
    soundcloud = models.URLField(blank=True)
    types = models.CharField(max_length=20, choices=[('Centre', 'Centre'), ('School', 'School'), ('Store', 'Store'), ('Pilgrimage', 'Pilgrimage'), ('Charity', 'Charity')])
    logo = models.ImageField(upload_to='logos/', help_text='Must be a height, width of 200px and image size under 20 Kilobytes.')
    photo_main = models.ImageField(upload_to='photos/', default='photos/', help_text='Must be a height of 300px.')
    photo_1 = models.ImageField(upload_to='photos/', default='photos/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/', default='photos/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/', default='photos/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/', default='photos/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/', default='photos/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.logo:
            if(self.logo.file.size > 20000):
             raise ValidationError(f'The image is {self.logo.file.size / 1000} Kilobytes. Must be 20 Kilobytes or less.')

            w, h = get_image_dimensions(self.logo)
            if w != 200:
                raise ValidationError("The logo is %i pixel wide. Must be 200px." % w)
            if h != 200:
                raise ValidationError("The logo is %i pixel high. Must be 200px." % h)

        if self.photo_main:
            h = get_image_dimensions(self.photo_main)
            if h != 300:
                raise ValidationError("The main profile image is %i pixel height. Must be 300px." % h)
            
    
    def __str__(self):
        return self.name
