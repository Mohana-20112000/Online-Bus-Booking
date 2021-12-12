from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .serializers import *
from . models import *


# Create your views here.

@api_view(['GET'])
def TravelList(request):
    travel = Travel.objects.all()
    serializer = TravelSerializer(travel, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TravelDetail(request, pk):
    travel = Travel.objects.get(id=pk)
    serializer = TravelSerializer(travel)
    return Response(serializer.data)

@api_view(['POST'])
def addTravel(request):
    serializer = TravelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateTravel(request,pk):
    travel = Travel.objects.get(id=pk)
    serializer = TravelSerializer(instance=travel,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTravel(request, pk):
    travel = Travel.objects.get(id=pk)
    travel.delete()
    return Response("Travels deleted successfully!")

#-------------------------------------------------------------

@api_view(['GET'])
def BookingList(request):
    book = Booking.objects.all()
    serializer =BookingSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def BookingDetail(request,pk):
    book = Booking.objects.get(id=pk)
    serializer = BookingSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])
def addBooking(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateBooking(request,pk):
    book = Booking.objects.get(id=pk)
    serializer = BookingSerializer(instance=book,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBooking(request,pk):
    book = Booking.objects.get(id=pk)
    book.delete()
    return Response("Booking Cancelled Successfully!")
