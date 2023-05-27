from . import views
from django.urls import path


urlpatterns = [
    path('', views.Seats.as_view(), name='home')
]