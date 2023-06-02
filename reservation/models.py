from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'available'), (1, 'reserved'))


class Seat(models.Model):
    seat_id = models.IntegerField(unique=True, null=False)
    num_of_seats = models.IntegerField(unique=False, null=False)
    seat_cost = models.IntegerField(unique=False, null=False)
    seat_image = CloudinaryField('image', default='placeholder')
    total_tables = models.IntegerField(unique=False, null=False, default=0)

    class Meta:
        ordering = ['seat_id']
    
    def __str__(self):
        return str(self.seat_id)


class Booking(models.Model):
    first_name = models.CharField(max_length=25,null=False)
    last_name = models.CharField(max_length=25,null=False)
    date_booked = models.DateTimeField(auto_now=True)
    seat_booked = models.IntegerField(unique=True, null=False)
    class Meta:
        ordering = ['date_booked']
    
    def __str__(self):
        return str(self.first_name)