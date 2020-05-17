# Generated by Django 3.0.6 on 2020-05-17 13:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('language', models.CharField(default='English', max_length=200)),
                ('is_online', models.BooleanField(default=False)),
                ('link', models.URLField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organisations.Organisation')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teachers.Teacher')),
            ],
        ),
    ]