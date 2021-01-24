from rest_framework import serializers
from .models import *

from django.http import JsonResponse

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Postnews
        fields =('__all__')
class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transfer
        fields=('__all__')


        



