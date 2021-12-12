from django.urls import path
from . import views

urlpatterns = [
    path('travel-details/',views.TravelList,name='travel-details'),
    path('travel-details/<int:pk>/',views.TravelDetail,name='travel-detail'),
    path('add-travel/',views.addTravel,name='add-travel'),
    path('update-travel/<int:pk>/',views.updateTravel,name='update-travel'),
    path('delete-travel/<int:pk>/',views.deleteTravel,name='delete-travel'),
    path('booking-details/',views.BookingList,name='booking-details'),
    path('booking-details/<int:pk>/',views.BookingDetail,name='booking-detail'),
    path('add-booking/',views.addBooking,name='add-booking'),
    path('update-booking/<int:pk>/',views.updateBooking,name='update-booking'),
    path('delete-booking/<int:pk>/',views.deleteBooking,name='delete-booking'),
    
]