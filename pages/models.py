from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Page(models.Model):
    slug = models.SlugField(unique=True, null=True)
    title = models.CharField(max_length=30)
    sub_heading = models.CharField(max_length=100, blank=True)
    text = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title