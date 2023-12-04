from django.test import TestCase
from .models import Seat

class TestModels(TestCase):

    def setUp(self):
        """
        Create the Seat objects for testing
        """
        self.seat0 = Seat.objects.create(seat_code='T001', seat_desc='Seat 0 created', seat_persons=3, seats_max=4)    

    def test_seat_create(self):
        self.assertEqual(Seat.objects.count(), 2)