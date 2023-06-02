# Generated by Django 3.2.19 on 2023-06-01 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20230528_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('date_booked', models.DateTimeField(auto_now=True)),
                ('seat_booked', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['date_booked'],
            },
        ),
        migrations.DeleteModel(
            name='Bookings',
        ),
    ]
