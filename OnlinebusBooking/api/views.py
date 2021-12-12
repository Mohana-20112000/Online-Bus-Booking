from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import *
from . models import *
# Create your views here.

@api_view(['GET'])
def UserLoginList(request):
    UserLogins = UserLogin.objects.all()
    serializer =UserLoginSerializer(UserLogins, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UserLoginDetail(request,pk):
    userlogin = UserLogin.objects.get(id=pk)
    serializer = UserLogin(userlogin)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserLogin(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateUser(request,pk):
    User = UserLogin.objects.get(id=pk)
    serializer = UserLogin(instance=User,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request,pk):
    user = UserLogin.objects.get(id=pk)
    user.delete()
    return Response("User Deleted Successfully!")

# Create your views here.------------------------------------------------
@api_view(['GET'])
def LocationList(request):
    location = Location.objects.all()
    serializer =LocationSerializer(location, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def LocationDetail(request,pk):
    locdet = Location.objects.get(id=pk)
    serializer = Location(locdet)
    return Response(serializer.data)

@api_view(['POST'])
def addLocation(request):
    serializer = Location(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# @api_view(['POST'])
# def updateLocation(request,pk):
#     loc = Location.objects.get(id=pk)
#     serializer = Location(instance=loc,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

@api_view(['DELETE'])
def deleteLocation(request,pk):
    local = Location.objects.get(id=pk)
    local.delete()
    return Response("Location Deleted Successfully!")


