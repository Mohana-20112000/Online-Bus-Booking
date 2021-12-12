from django.db import models
from api.models import *

# Create your models here.
class Travel(models.Model):
    TravelsName = models.CharField(max_length=100, null=False, blank=False)
    DriverName = models.CharField(max_length=100, null=False, blank=False)
    BusPlateNo = models.CharField(max_length=100, null=False, blank=False)
    DriverPhone = models.CharField(max_length=100, null=False, blank=False)
    DriverCity = models.CharField(max_length=100, null=False, blank=False)
    CostPerSeat = models.IntegerField(null=False, blank=False)
    TravelsFeatures = models.TextField(null=False, blank=False)
    BusRatings = models.IntegerField(null=False, blank=False)
    TravelsLocation = models.ForeignKey(Location,related_name="travelslocation", on_delete=models.CASCADE)
    def __str__(self):
        return self.TravelsName



class Booking(models.Model):
    BookingDate = models.DateField(null=False, blank=False)
    BookingTime = models.TimeField(null=False, blank=False)
    BookedUser = models.ForeignKey(UserLogin,related_name="bookeduser",on_delete=models.CASCADE,default=None)
    BookedTravels = models.ForeignKey(Travel,related_name="bookedtravel", on_delete=models.CASCADE,default=None)
    BookingStatus = models.CharField(max_length=100, null=False, blank=False,default='Pending')
    BookingCreatedAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.BookedUser.UserName}'s Booking"
