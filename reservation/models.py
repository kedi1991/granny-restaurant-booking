from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'available'), (1, 'reserved'))


class Seat(models.Model):
    seat_code = models.CharField(primary_key=True, default='T000', max_length=4, unique=True, null=False)
    seat_desc = models.CharField(max_length=120, unique=False, null=False, default='No description available')
    seat_persons = models.IntegerField(unique=False, null=False, default=2)
    seats_max = models.IntegerField(unique=False, null=False, default=2)
    seat_image = CloudinaryField('image', default='placeholder')


    class Meta:
        ordering = ['seat_code']
    
    def __str__(self):
        return str(self.seat_code)

class Booking(models.Model):
    booking_code = models.CharField(max_length=5)
    booking_client_name = models.CharField(max_length=30, null=False)
    booking_client_phone = models.CharField(max_length=15, null=False)
    booking_client_email = models.EmailField(null=False)
    booking_date = models.DateTimeField(auto_now=False)

    class Meta:
        ordering = ['booking_code']
    
    def __str__(self):
        return str(self.booking_code)