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
        getdata = Post.object.all().orderby('-id')[:15]
        serializer =PostSerializers(getdata, many=True)
        return JsonResponse({'message': 'success', 'data':serializers.data}, safe=False)
    elif request.method=='POST':
        data =JSONParser().parser(request)
        serializer=PostSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'success', 'data':serializer.da})