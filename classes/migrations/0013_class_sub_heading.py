# Generated by Django 3.0.6 on 2020-05-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0012_auto_20200527_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='sub_heading',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
