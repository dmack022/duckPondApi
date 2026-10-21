from django.shortcuts import render
from .models import Pond
from rest_framework import generics, viewsets
from .serializers import PondSerializer


class PondViewSet(viewsets.ModelViewSet):
    queryset = Pond.objects.all()
    serializer_class = PondSerializer
