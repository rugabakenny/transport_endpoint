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
def btransfer(request):
    if request.method == 'GET':
        reg = Transfer.objects.all()
        serializer = TransferSerializer(reg, many=True)
        return JsonResponse(serializer.data,safe=False)
    

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TransferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors,status=400)