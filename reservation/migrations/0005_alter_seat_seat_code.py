# Generated by Django 3.2.19 on 2023-06-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_auto_20230605_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_code',
            field=models.CharField(default='TXXX', max_length=4, unique=True),
        ),
    ]
