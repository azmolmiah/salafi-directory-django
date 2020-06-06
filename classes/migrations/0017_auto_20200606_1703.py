# Generated by Django 3.0.6 on 2020-06-06 16:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0016_auto_20200528_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='days',
        ),
        migrations.RemoveField(
            model_name='class',
            name='time',
        ),
        migrations.AddField(
            model_name='class',
            name='date_And_Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 16, 3, 18, 413209, tzinfo=utc)),
        ),
    ]
