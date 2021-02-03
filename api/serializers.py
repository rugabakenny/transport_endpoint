from rest_framework import serializers
from .models import *

from django.http import JsonResponse

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Postnews
        fields =('__all__')

class GorillaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Gorilla
        fields =('__all__')


class LakeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Lake
        fields =('__all__')

class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields =('__all__')

class MountainSerializers(serializers.ModelSerializer):
    class Meta:
        model=Mountain
        fields =('__all__')

        



