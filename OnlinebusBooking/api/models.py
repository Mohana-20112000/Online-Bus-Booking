from django.db import models

# Create your models here.
class UserLogin(models.Model):
    
    UserName = models.CharField(max_length=100, null=False, blank=False)
    Email = models.EmailField(max_length=100, null=False, blank=False)
    Phone = models.CharField(max_length=100, null=False, blank=False)
    City = models.CharField(max_length=100, null=False, blank=False)
    Age = models.IntegerField(null=False, blank=False)
    Gender = models.CharField(max_length=100, null=False, blank=False)
    UserPassword = models.CharField(max_length=100,null=True,blank=False)

    def __str__(self):
        return self.UserName

class Location(models.Model):
    
    LocationName = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.LocationName
