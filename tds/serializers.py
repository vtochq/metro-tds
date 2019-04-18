from rest_framework import serializers
from .models import *

class displaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Display
        fields = '__all__'