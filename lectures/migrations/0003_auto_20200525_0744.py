# Generated by Django 3.0.6 on 2020-05-25 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_auto_20200525_0732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='expiration',
            new_name='expiration_days',
        ),
    ]