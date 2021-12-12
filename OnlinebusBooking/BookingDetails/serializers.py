from . models import *
from rest_framework import serializers
from api.serializers import LocationSerializer
from .serializers import *
from api.serializers import UserLoginSerializer

class TravelSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True, read_only=True)
    class Meta:
        model = Travel
        fields = '__all__'
        depth = 1

class BookingSerializer(serializers.ModelSerializer):
    travel = TravelSerializer(many=False, read_only=True)
    user = UserLoginSerializer(many=True, read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'
        depth = 1