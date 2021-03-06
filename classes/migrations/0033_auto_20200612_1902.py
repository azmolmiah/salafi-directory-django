# Generated by Django 3.0.6 on 2020-06-12 18:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0032_auto_20200612_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='description',
            field=models.TextField(help_text='Must be equal 132 characters.', max_length=132, validators=[django.core.validators.MinLengthValidator(132)]),
        ),
        migrations.AlterField(
            model_name='class',
            name='link',
            field=models.URLField(blank=True, help_text='Link to online class.'),
        ),
        migrations.AlterField(
            model_name='class',
            name='photo',
            field=models.ImageField(default='classes/', help_text='Must be a height and width of 200px.', upload_to='classes/'),
        ),
        migrations.AlterField(
            model_name='class',
            name='sub_Heading',
            field=models.CharField(blank=True, help_text='Max 30 characters', max_length=30),
        ),
        migrations.AlterField(
            model_name='class',
            name='title',
            field=models.CharField(help_text='Max 30 characters', max_length=28, unique=True),
        ),
    ]
