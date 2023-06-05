from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.Seats.as_view(), name='home'),
    path('<slug:seat_code>/', views.Bookings.as_view(), name='bookings'),

]