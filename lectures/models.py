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
    account = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.CASCADE)
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, null=True)
    teacher = models.ManyToManyField(Teacher)
    title = models.CharField(max_length=28)
    description = models.TextField(max_length=132)
    date_And_Time = models.DateTimeField(default=datetime.today)
    expiration_Date_And_Time = models.DateTimeField(default=one_day)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    language = models.CharField(max_length=200, default='English')
    is_online = models.BooleanField(default=False)
    link = models.URLField(blank=True)
    photo = models.ImageField(upload_to='lectures/', default='lectures/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def is_live(self):
        return datetime.now().timestamp() >= self.date_And_Time.timestamp() and datetime.now().timestamp() <= self.expiration_Date_And_Time.timestamp()

    def clean(self):
        if self.date_And_Time.date() > self.expiration_Date_And_Time.date():
            raise ValidationError("Date cannot be ahead of expiration date")

        if self.date_And_Time.date() == self.expiration_Date_And_Time.date() and self.date_And_Time.time() > self.expiration_Date_And_Time.time():
            raise ValidationError("Time cannot be ahead of expiration time")

    def __str__(self):
        return self.title
