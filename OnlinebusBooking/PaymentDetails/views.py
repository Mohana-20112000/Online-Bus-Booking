from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import *
from . models import *

# Create your views here.

@api_view(['GET'])
def PaymentList(request):
    pay = Payment.objects.all()
    serializer =PaymentSerializer(pay, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def PaymentDetail(request,pk):
    pay = Payment.objects.get(id=pk)
    serializer = PaymentSerializer(pay)
    return Response(serializer.data)

@api_view(['POST'])
def addPayment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# @api_view(['POST'])
# def updatePayment(request,pk):
#     pay = Payment.objects.get(id=pk)
#     serializer = PaymentSerializer(instance=pay,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

@api_view(['DELETE'])
def deletePayment(request,pk):
    pay = Payment.objects.get(id=pk)
    pay.delete()
    return Response("Booking Cancelled Successfully!")

