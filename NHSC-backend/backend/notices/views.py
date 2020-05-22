from django.shortcuts import render
from rest_framework import viewsets
from .models import Notices
from .serializers import NoticeSerializer

# Create your views here.
class NoticeView(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notices.objects.all()