# Generated by Django 3.0.6 on 2020-05-27 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0011_class_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='author',
            new_name='account',
        ),
    ]