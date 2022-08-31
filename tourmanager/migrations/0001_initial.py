# Generated by Django 3.0.2 on 2020-01-21 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_name', models.CharField(max_length=30)),
                ('map_location', models.CharField(blank=True, max_length=255)),
                ('destination_image', models.ImageField(upload_to='assets/img/destinatiions/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('map_location', models.CharField(blank=True, max_length=255)),
                ('region_featured_image', models.ImageField(upload_to='assets/img/regions')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('min_number_of_people', models.CharField(max_length=4)),
                ('max_number_of_people', models.CharField(max_length=4)),
                ('tour_price', models.FloatField(max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TourData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_days', models.CharField(blank=True, max_length=3)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tourmanager.Destinations')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tourmanager.Regions')),
                ('tourid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tourmanager.Tours')),
            ],
        ),
        migrations.AddField(
            model_name='destinations',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tourmanager.Regions'),
        ),
    ]
