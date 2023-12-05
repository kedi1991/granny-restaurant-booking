from django.test import TestCase
from .models import Booking

class TestBookingModel(TestCase):

    def setUp(self):
        """
        Create the Booking objects for testing
        """
        self.Booking0 = Booking.objects.create(booking_code='T001', booking_client_name='henry', booking_client_phone='077445555', booking_client_email='henry@gmail.com', booking_date='2023-12-12 00:00')

    def test_booking_create(self):
        self.assertEqual(Booking.objects.count(), 1)

    def test_booking_cancel(self):
        self.Booking0.delete()
        self.assertEqual(Booking.objects.count(), 0)

    def test_Booking_edit(self):
        booking = Booking.objects.get(booking_code='T001')
        booking.booking_client_phone = '3466110099'
        booking.save()
        new_booking = Booking.objects.get(booking_code='T001')
        self.assertEqual(new_booking.booking_client_phone, '3466110099')