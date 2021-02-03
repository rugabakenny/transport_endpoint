from django.shortcuts import render
from django. http import HttpResponse
from .models import*
from .serializers import*
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
def welcome(request):
    return HttpResponse('get home')


def posts(request):
    if request.method =='GET':
        getdata = Postnews.objects.all().order_by('-id')[:40]
        serializer =PostSerializers(getdata, many=True)
        return JsonResponse({'message': 'success', 'data':serializer.data}, safe=False)
    elif request.method=='POST':
        data =JSONParser().parser(request)
        serializer=PostSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'success', 'data':serializer.da})


def btgorilla(request):
    if request.method =='GET':
        getdata = Gorilla.objects.all().order_by('-id')[:40]
        serializer =GorillaSerializers(getdata, many=True)
        return JsonResponse({'message': 'success', 'data':serializer.data}, safe=False)
    elif request.method=='POST':
        data =JSONParser().parser(request)
        serializer=GorillaSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'success', 'data':serializer.da})

def btlake(request):
    if request.method =='GET':
        getdata = Lake.objects.all().order_by('-id')[:40]
        serializer =LakeSerializers(getdata, many=True)
        return JsonResponse({'message': 'success', 'data':serializer.data}, safe=False)
    elif request.method=='POST':
        data =JSONParser().parser(request)
        serializer=LakeSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'success', 'data':serializer.da})

def bthotel(request):
    if request.method =='GET':
        getdata = Hotel.objects.all().order_by('-id')[:40]
        serializer =HotelSerializers(getdata, many=True)
        return JsonResponse({'message': 'success', 'data':serializer.data}, safe=False)
    elif request.method=='POST':
        data =JSONParser().parser(request)
        serializer=HotelSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'success', 'data':serializer.da})


def btmountain(request):
    if request.method =='GET':
        getdata = Mountain.objects.all().order_by('-id')[:40]
        serializer =MountainSerializers(getdata, many=True)
        return JsonResponse({'message': 'success', 'data':serializer.data}, safe=False)
    elif request.method=='POST':
        data =JSONParser().parser(request)
        serializer=MountainSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'success', 'data':serializer.da})


