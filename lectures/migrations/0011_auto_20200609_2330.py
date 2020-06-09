# Generated by Django 3.0.6 on 2020-06-09 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0016_auto_20200606_2128'),
        ('lectures', '0010_auto_20200607_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='teacher',
        ),
        migrations.AddField(
            model_name='lecture',
            name='teacher',
            field=models.ManyToManyField(to='teachers.Teacher'),
        ),
    ]
