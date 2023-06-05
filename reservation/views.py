from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Seat, Booking


class Seats(generic.ListView):
    model = Seat
    queryset = model.objects.all()
    template_name = 'index.html'
    
    

class Bookings(View):
    def get(self, request, seat_id, *args, **kwargs):
        model = Booking
        queryset = model.objects.all()
        bookings = get_object_or_404(queryset, id=seat_id)

        mydata = bookings

        return render(request, 
        'bookings.html',
        {
            "first_name":"Henry kedi",
            "last_name": "Okurut",
            "date_booked": "23/1/2009T00:00:00",
            "seat_booked": "True",
            "id": "is it",
        },
        )