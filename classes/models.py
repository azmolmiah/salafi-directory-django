from django.db import models
from django.utils import timezone
from organisations.models import Organisation
from teachers.models import Teacher


class Class(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField()
    time = models.TimeField(default=timezone.now)
    days = models.CharField(max_length=20, default='Monday', choices=[(
        'Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')])
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    language = models.CharField(max_length=200, default='English')
    is_online = models.BooleanField(default=False)
    link = models.URLField(blank=True)
    photo = models.ImageField(upload_to=f'classes/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
