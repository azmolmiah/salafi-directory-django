from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from organisations.models import Organisation
from teachers.models import Teacher
from django.contrib.auth import get_user_model

def one_day():
  return datetime.today() + timedelta(days=1)
class Lecture(models.Model):
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=datetime.today)
    time = models.TimeField(default=timezone.now)
    expiration_date = models.DateField(default=one_day)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    language = models.CharField(max_length=200, default='English')
    is_online = models.BooleanField(default=False)
    link = models.URLField(blank=True)
    photo = models.ImageField(upload_to='lectures/', default='lectures/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def clean(self):
      if self.date > self.expiration_date:
        raise ValidationError("Date cannot be ahead of expiration date")

    def __str__(self):
        return self.title