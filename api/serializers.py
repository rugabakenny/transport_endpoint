from rest_framework import serializers
from .models import *
from django.http import JsonResponse
class PostSerializers(serializers.modelSerializers):
    class Meta:
        model =Post
        fields =('__all__')
    def create(self,validated_data):
        title =validated_data('title')
        postedby =validated_data('posted_by')
        description =validated_data('description')

        



