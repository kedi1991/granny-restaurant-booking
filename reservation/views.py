from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Seat, Booking


class Seats(generic.ListView):
    model = Seat
    queryset = model.objects.all()
    template_name = 'index.html'
    
    
class Bookings(View):
    def get(self, request, seat_code, *args, **kwargs):
        """
        This will get the details of the 
        """
        model = Booking
        booking_code = seat_code
        queryset = model.objects.all()
        bookings = get_object_or_404(queryset, booking_code=booking_code)

        mydata = bookings

        return render(request, 
        'bookings.html',
        {
            "first_name": booking_code,
            "last_name": "Okurut",
            "date_booked": "23/1/2009T00:00:00",
            "seat_booked": "True",
            "id": "is it",
        },
        )

