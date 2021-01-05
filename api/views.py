from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.httpResponse import HttpResponse
from .models import *
from .Serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
def Welcome(request):
    return HttpResponse('get api')

def posts(request):
    if request.method =='GET':
        getdata =post.objects.all().order_by('-id')[:15]
        Serializer =PostSerializers(getdata,many=true)
        return JsonResponse=({'message':'success','data':serializer.data, safe=False})
    elif request.method =='POST':
        data=JSONParser().parse(request)
        Serializer=PostSerializers(data=data)
        if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message':'success','data':serializer.data, status=201})