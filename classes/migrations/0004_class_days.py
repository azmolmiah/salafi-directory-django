# Generated by Django 3.0.6 on 2020-05-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20200519_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='days',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=20),
        ),
    ]