# Generated by Django 3.0.6 on 2020-06-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0013_auto_20200610_0710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='sub_Heading',
        ),
        migrations.AlterField(
            model_name='lecture',
            name='title',
            field=models.CharField(max_length=26),
        ),
    ]
