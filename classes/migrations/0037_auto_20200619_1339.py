# Generated by Django 3.0.6 on 2020-06-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0036_auto_20200619_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='sub_Heading',
            field=models.CharField(blank=True, help_text='Max 25 characters', max_length=25),
        ),
    ]
