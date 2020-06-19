# Generated by Django 3.0.6 on 2020-06-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0003_auto_20200613_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='photo',
            field=models.ImageField(default='lectures/', help_text='Must be a height, width of 200px and image size under 20 Kilobytes.', upload_to='lectures/'),
        ),
    ]
