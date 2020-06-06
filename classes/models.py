from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from organisations.models import Organisation
from teachers.models import Teacher

class Class(models.Model):
    account = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    sub_Heading = models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=132, help_text='Maximum of 132 characters.')
    date_And_Time = models.DateTimeField(default=timezone.now, help_text='The day and time will be used for every week.')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text='Eg: 0 = free / 1.22 = 1.22')
    language = models.CharField(max_length=200, default='English')
    is_online = models.BooleanField(default=False)
    link = models.URLField(blank=True)
    photo = models.ImageField(upload_to='classes/', default='classes/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title