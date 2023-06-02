from . import views
from django.urls import path


urlpatterns = [
    path('', views.Seats.as_view(), name='home'),
    path('booking/<seat_id>/', views.Bookings.as_view(), name='bookings')
]