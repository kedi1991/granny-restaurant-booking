from django.shortcuts import render, get_object_or_404, redirect
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
        Opens the form to fill in reservation details
        """
        model = Booking
        booking_code = seat_code
        queryset = model.objects.all()
        # bookings = get_object_or_404(queryset, booking_code=booking_code)


        return render(request, 
        'bookings.html',
        {
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


class ViewMyReservations(View):
    def get(self, request, username, *args, **kwargs):
        """
        Displays a list of all reservations made with the restaurant.
        """
        model = Booking
        queryset = model.objects.filter(booking_client_name=username)
        template_name = 'my_bookings.html'

        return render(
            request, 
            'my_bookings.html', 
            {'my_reservations': queryset
            }
            )

    def post(self, request, username, *args, **kwargs):
        """
        This will delete an entry from the users's booking table
        """
        model = Booking
        
        queryset = model.objects.filter(id=entry_id)
        bookings = get_object_or_404(queryset)
        bookings.delete()
       
        return redirect('my_bookings')

class EditMyReservations(View):
    def get(self, request, booking_id, *args, **kwargs):
        """
        Displays the reservation to be edited.
        """
        model = Booking

        instance = Booking.objects.get(id=booking_id)
        form = BookingForm(instance=instance)
        context = {'form': form}

        template_name = 'edit_booking.html'

        return render(request, 'edit_booking.html', context)

    def post(self, request, booking_id, *args, **kwargs):
        """
        This will save an entry after editing
        """
        model = Booking
        instance = model.objects.get(id=booking_id)
        form = BookingForm(request.POST, instance=instance)
        
        if form.is_valid():
            form.instance.full_clean()
            form.save()
            return redirect('my_bookings')

    
    
