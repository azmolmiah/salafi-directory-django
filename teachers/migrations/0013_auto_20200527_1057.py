# Generated by Django 3.0.6 on 2020-05-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0012_auto_20200527_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='_teachers',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teachers',
            field=models.ManyToManyField(blank=True, null=True, related_name='_teacher_teachers_+', to='teachers.Teacher'),
        ),
    ]
