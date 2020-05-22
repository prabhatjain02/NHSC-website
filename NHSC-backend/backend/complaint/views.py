from django.shortcuts import render
from rest_framework import viewsets
from .models import Complaint
from .serializers import ComplaintSerializer

# Create your views here.
class ComplaintView(viewsets.ModelViewSet):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()