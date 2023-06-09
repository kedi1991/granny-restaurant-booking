# Generated by Django 3.2.19 on 2023-06-05 15:48

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_code', models.CharField(max_length=5)),
                ('booking_client_name', models.CharField(max_length=30)),
                ('booking_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['booking_code'],
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_code', models.CharField(default='TXXX', max_length=4, unique=True)),
                ('seat_desc', models.CharField(default='No description available', max_length=120)),
                ('seat_persons', models.IntegerField(default=2)),
                ('seats_max', models.IntegerField(default=2)),
                ('seat_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['seat_code'],
            },
        ),
    ]
