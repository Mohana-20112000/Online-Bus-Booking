from django.db import models
from BookingDetails.models import Booking

# Create your models here.
class Payment(models.Model):
    
    AccountHolderName = models.CharField(max_length=100, null=False, blank=False)
    AccountNumber= models.CharField(max_length=100, null=False, blank=False)
    ExpiryDate = models.CharField(max_length=100, null=False, blank=False)
    UserPassword = models.CharField(max_length=100,null=True,blank=False)
    BookedId = models.ForeignKey(Booking,related_name="bookedid", on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f"{self.BookedId.BookedUser}'s Payment"