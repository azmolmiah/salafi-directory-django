# Generated by Django 3.0.6 on 2020-06-12 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='description',
            field=models.TextField(help_text='Must be equal 132 characters.', max_length=132, validators=[django.core.validators.MinLengthValidator(132)]),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='link',
            field=models.URLField(blank=True, help_text='Link to online class.'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Eg: 0 = free / 1.22 = 1.22', max_digits=6),
        ),
    ]