from django.shortcuts import render
from rest_framework import viewsets
from .models import Meeting
from .serializers import MeetingSerializer

# Create your views here.
class MeetingView(viewsets.ModelViewSet):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()