# Generated by Django 3.0.6 on 2020-06-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0014_auto_20200527_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
