# Generated by Django 3.0.6 on 2020-05-22 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20200522_0257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='photo',
        ),
    ]