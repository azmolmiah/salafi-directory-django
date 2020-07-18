from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.core.files.images import get_image_dimensions

from organisations.models import Organisation
from teachers.models import Teacher


class Class(models.Model):
    account = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.CASCADE)
    organisation = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=28, help_text='Max 30 characters')
    sub_Heading = models.CharField(
        max_length=40, blank=True, help_text='Max 40 characters')
    description = models.TextField(
        max_length=132, help_text='Must be equal 132 characters.', validators=[MinLengthValidator(132)])
    date_And_Time = models.DateTimeField(
        default=timezone.now, help_text='The day and time will be used for every week.Please, add time difference if behind or takeaway if ahead of server time.')
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, help_text='Eg: 0 = free / 1.22 = 1.22')
    language = models.CharField(max_length=20, default='English')
    is_online = models.BooleanField(default=False)
    link = models.URLField(blank=True, help_text='Link to online class.')
    photo = models.ImageField(upload_to='classes/', default='classes/',
                              help_text='Must be a height, width of 200px and image size under 25 Kilobytes.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def is_live(self):
        return self.date_And_Time.day == datetime.now().day and self.date_And_Time.hour == datetime.now().hour
    
    def not_started(self):
        return datetime.now().timestamp() < self.date_And_Time.timestamp()

    def clean(self):
        if(self.photo.file.size > 25000):
            raise ValidationError(
                f'The image is {self.photo.file.size / 1000} Kilobytes. Must be 25 Kilobytes or less.')

        w, h = get_image_dimensions(self.photo)
        if w != 200:
            raise ValidationError(
                "The image is %i pixel wide. Must be 200px." % w)
        if h != 200:
            raise ValidationError(
                "The image is %i pixel high. Must be 200px." % h)

    def __str__(self):
        return self.title
