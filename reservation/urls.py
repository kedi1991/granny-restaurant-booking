from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.Seats.as_view(), name='home'),
    path('<slug:seat_code>/', views.Bookings.as_view(), name='bookings'),
    path('<slug:username>', views.ViewMyReservations.as_view(), name='my_bookings'),    
    path('<slug:id>', views.ViewMyReservations.as_view(), name='del_bookings'),   
    path('edit/<booking_id>', views.EditMyReservations.as_view() , name='edit_booking'),     
]