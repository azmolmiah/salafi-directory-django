# Generated by Django 3.0.6 on 2020-05-22 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrators', '0002_auto_20200522_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrator',
            name='organisation',
        ),
    ]
