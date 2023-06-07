from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_code', 'booking_client_name', 'booking_client_email', 'booking_client_phone', 'booking_date',)
        widgets = {
            'booking_date': forms.DateTimeInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            )
            
        }
       


    