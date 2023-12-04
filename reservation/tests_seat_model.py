from django.test import TestCase
from .models import Seat

class TestSeatModel(TestCase):

    def setUp(self):
        """
        Create the Seat objects for testing
        """
        self.seat0 = Seat.objects.create(seat_code='T001', seat_desc='Seat 0 created', seat_persons=3, seats_max=4)
        self.seat1 = Seat.objects.create(seat_code='T002', seat_desc='Seat 1 created', seat_persons=2, seats_max=3)

    def test_seat_create(self):
        self.assertEqual(Seat.objects.count(), 2)