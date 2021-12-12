from django.urls import path
from . import views

urlpatterns = [
    path('user-details/',views.UserLoginList,name='user-details'),
    path('user-details/<int:pk>/',views.UserLoginDetail,name='user-detail'),
    path('add-user/',views.addUser,name='add-user'),
    path('update-user/<int:pk>/',views.updateUser,name='update-user'),
    path('delete-user/<int:pk>/',views.deleteUser,name='delete-user'),
    path('location-details/',views.LocationList,name='location-details'),
    path('location-details/<int:pk>/',views.LocationDetail,name='location-detail'),
    path('add-location/',views.addLocation,name='add-location'),
    path('delete-location/<int:pk>/',views.deleteLocation,name='delete-location'),

]