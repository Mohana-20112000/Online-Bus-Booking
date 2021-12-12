from types import TracebackType
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Travel)
admin.site.register(Booking)