from rest_framework import serializers
from .models import Joining

class JoiningSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Joining
        fields = '__all__'