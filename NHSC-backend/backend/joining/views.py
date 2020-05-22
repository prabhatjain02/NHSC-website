from django.shortcuts import render
from rest_framework import viewsets
from .models import Joining
from .serializers import JoiningSerializer

# Create your views here.
class JoiningView(viewsets.ModelViewSet):
    serializer_class = JoiningSerializer
    queryset = Joining.objects.all()