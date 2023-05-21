from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'available'), (1, 'reserved'))


class Seat(models.Model):
    seat_id = models.IntegerField(unique=True, null=False)
    num_of_seats = models.IntegerField(unique=False, null=False)
    seat_cost = models.IntegerField(unique=False, null=False)
    seat_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['seat_id']
    
    def __str__(self):
        return self.seat_id
