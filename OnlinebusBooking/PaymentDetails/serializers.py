from . models import *
from rest_framework import serializers
from BookingDetails.serializers import *
class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(many=False, read_only=True)
    class Meta:
        model = Payment
        fields = '__all__'
        depth = 1
