# Generated by Django 4.1.13 on 2024-10-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('license_plate', models.CharField(max_length=20, unique=True)),
                ('manufacturer', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('capacity', models.PositiveIntegerField()),
                ('current_location_lat', models.FloatField(blank=True, null=True)),
                ('current_location_lng', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('maintenance', 'Under Maintenance')], default='active', max_length=20)),
            ],
        ),
    ]
