# Generated by Django 3.2.9 on 2021-11-06 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carid', models.CharField(max_length=200, null=True)),
                ('lane', models.CharField(max_length=200, null=True)),
                ('uniqueNumber', models.CharField(max_length=200, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('front_license_number', models.CharField(blank=True, max_length=200, null=True)),
                ('front_license_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('front_car_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('end_license_number', models.CharField(blank=True, max_length=200, null=True)),
                ('end_license_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('end_car_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('velocity', models.FloatField(blank=True, null=True)),
                ('number_axis', models.IntegerField(blank=True, null=True)),
                ('totalweight', models.FloatField(blank=True, null=True)),
                ('listweight', models.CharField(blank=True, max_length=1024, null=True)),
                ('maxD', models.FloatField(blank=True, null=True)),
                ('listD', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]
