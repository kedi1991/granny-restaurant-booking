from django.shortcuts import render
from django.views import generic
from .models import Seat


class Seats(generic.ListView):
    model = Seat
    queryset = model.objects.all()

    template_name = 'index.html'
    paginate_by = 20
    
