# Generated by Django 3.0.6 on 2020-05-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_remove_class_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='photo',
            field=models.ImageField(default='classes/', upload_to='classes/'),
        ),
    ]
