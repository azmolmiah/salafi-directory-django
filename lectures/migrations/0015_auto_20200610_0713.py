# Generated by Django 3.0.6 on 2020-06-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0014_auto_20200610_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='title',
            field=models.CharField(max_length=27),
        ),
    ]
