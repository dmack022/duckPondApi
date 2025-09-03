from django.shortcuts import render
from rest_framework import generics
from .models import Duck
from .serializers import DuckSerializer

class DucksListCreate(generics.ListCreateAPIView):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer