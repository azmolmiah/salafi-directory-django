# Generated by Django 3.0.6 on 2020-05-25 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0004_auto_20200525_0755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='dateTime',
            new_name='datetime',
        ),
    ]
