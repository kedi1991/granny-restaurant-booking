from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Seat, Booking
from .forms import BookingForm


class Seats(generic.ListView):
    model = Seat
    queryset = model.objects.all()
    template_name = 'index.html'
    
    
class Bookings(View):
    def get(self, request, seat_code, *args, **kwargs):
        """
        This will get the details of the booking
        """
        model = Booking
        booking_code = seat_code
        queryset = model.objects.all()
        # bookings = get_object_or_404(queryset, booking_code=booking_code)


        return render(request, 
        'bookings.html',
        {
            "first_name": booking_code,
            "last_name": "Okurut",
            "date_booked": "23/1/2009T00:00:00",
            "seat_booked": "True",
            "id": "is it",
            "booking_form": BookingForm(),
        },
        )

    def post(self, request, seat_code, *args, **kwargs):
        """
        This update get the Bookings table with information of the reservation made 
        """
        model = Booking
        booking_code = seat_code
        # queryset = model.objects.all()
        # bookings = get_object_or_404(queryset, booking_code=booking_code)

        booking_form = BookingForm(data=request.POST)

        # Proceed only if the data entered is valid
        if booking_form.is_valid():
            booking_form.instance.booking_client_name = request.user.username
            booking_form.instance.booking_code = seat_code
            
            booking_form.save(commit=True)

        else:
            booking_form = BookingForm()
        return render(request, 
        'bookings.html',
        {
            "booking_form": BookingForm(),
        },
        )
