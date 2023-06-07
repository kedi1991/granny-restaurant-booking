# Generated by Django 3.2.19 on 2023-06-06 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_booking_seat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='id',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_client_email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_client_phone',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_code',
            field=models.CharField(default='T000', max_length=4, primary_key=True, serialize=False, unique=True),
        ),
    ]