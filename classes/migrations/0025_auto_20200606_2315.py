# Generated by Django 3.0.6 on 2020-06-06 22:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0024_auto_20200606_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='date_And_Time',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='The day and time will be used for every week.'),
        ),
        migrations.AlterField(
            model_name='class',
            name='description',
            field=models.TextField(help_text='Maximum of 132 characters.', max_length=132),
        ),
        migrations.AlterField(
            model_name='class',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Eg: 0 = free / 1.22 = 1.22', max_digits=6),
        ),
    ]