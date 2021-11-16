# Generated by Django 3.1.13 on 2021-11-16 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planes', '0001_initial'),
        ('cities', '0003_auto_20211116_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Route name')),
                ('travel_times', models.PositiveSmallIntegerField(verbose_name='Travel Time')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city', verbose_name='Departing from a city')),
                ('planes', models.ManyToManyField(to='planes.Plane', verbose_name='List of Planes')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city', verbose_name='Arriving in a city')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
                'ordering': ['travel_times'],
            },
        ),
    ]