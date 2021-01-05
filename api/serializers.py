from rest_framework import serializers
from .models import *

from django.http import JsonResponse

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Posts
        fields =('__all__')


        



