# Generated by Django 3.0.6 on 2020-05-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0007_auto_20200522_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='logo',
            field=models.ImageField(upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='photo_1',
            field=models.ImageField(blank=True, default='photos/', upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='photo_2',
            field=models.ImageField(blank=True, default='photos/', upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='photo_3',
            field=models.ImageField(blank=True, default='photos/', upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='photo_4',
            field=models.ImageField(blank=True, default='photos/', upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='photo_5',
            field=models.ImageField(blank=True, default='photos/', upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='photo_main',
            field=models.ImageField(default='photos/', upload_to='photos/'),
        ),
    ]
