# Generated by Django 3.0.6 on 2020-05-22 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0008_auto_20200522_1615'),
        ('administrators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='organisation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='organisations.Organisation'),
        ),
    ]
