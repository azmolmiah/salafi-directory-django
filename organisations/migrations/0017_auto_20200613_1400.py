# Generated by Django 3.0.6 on 2020-06-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0016_auto_20200612_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='logo',
            field=models.ImageField(help_text='Must be a height and width of 200px.', upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='photo_main',
            field=models.ImageField(default='photos/', help_text='Must be a height of 300px.', upload_to='photos/'),
        ),
    ]
