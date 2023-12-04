from django.test import TestCase
from .models import Booking

class TestBookingModel(TestCase):

    def setUp(self):
        """
        Create the Booking objects for testing
        """
        self.Booking0 = Booking.objects.create(booking_code='T001', booking_client_name='henry', booking_client_phone='077445555', booking_client_email='henry@gmail.com', booking_date='2023-12-12 00:00')

    def test_booking_create(self):
        self.assertEqual(Booking.objects.count(), 2)