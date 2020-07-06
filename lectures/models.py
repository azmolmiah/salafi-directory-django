from datetime import datetime, timedelta
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.core.files.images import get_image_dimensions

from organisations.models import Organisation
from teachers.models import Teacher

def one_day():
    return datetime.today() + timedelta(days=1)

class Lecture(models.Model):
    account = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True)
    teacher = models.ManyToManyField(Teacher)
    title = models.CharField(max_length=28, help_text='Max 30 characters')
    description = models.TextField(max_length=132, help_text='Must be equal 132 characters.', validators=[MinLengthValidator(132)])
    date_And_Time = models.DateTimeField(default=datetime.today)
    expiration_Date_And_Time = models.DateTimeField(default=one_day)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text='Eg: 0 = free / 1.22 = 1.22')
    language = models.CharField(max_length=20, default='English')
    is_online = models.BooleanField(default=False)
    link = models.URLField(blank=True, help_text='Link to online class.')
    photo = models.ImageField(upload_to='lectures/', default='lectures/',
                              help_text='Must be a height, width of 200px and image size under 25 Kilobytes.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def is_live(self):
        return datetime.now().timestamp() >= self.date_And_Time.timestamp() and datetime.now().timestamp() <= self.expiration_Date_And_Time.timestamp()
    
    def not_started(self):
        return datetime.now().timestamp() < self.date_And_Time.timestamp()

    def clean(self):
        if self.date_And_Time.date() > self.expiration_Date_And_Time.date():
            raise ValidationError("Date cannot be ahead of expiration date")

        if self.date_And_Time.date() == self.expiration_Date_And_Time.date() and self.date_And_Time.time() >= self.expiration_Date_And_Time.time():
            raise ValidationError("Time cannot be ahead of expiration time")

        if(Lecture.objects.count() > 5 and self.pk is None):
            raise ValidationError(
                "You are only allowed five lectures. Please, edit or remove a lecture.")

        if(self.photo.file.size > 25000):
            raise ValidationError(
                f'The image is {self.photo.file.size / 1000} Kilobytes. Must be 25 Kilobytes or less.')

        w, h = get_image_dimensions(self.photo)
        if w != 200:
            raise ValidationError(
                "The image is %i pixel wide. Must be 200px" % w)
        if h != 200:
            raise ValidationError(
                "The image is %i pixel high. Must be 200px" % h)

    def __str__(self):
        return self.title
