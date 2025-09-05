from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Duck, Food, Flavor, DuckFlavor, FoodFlavor
from .serializers import DuckSerializer, FoodSerializer, FlavorSerializer, DuckFlavorSerializer, FoodFlavorSerializer

class DuckViewSet(viewsets.ModelViewSet):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FlavorViewSet(viewsets.ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer

class DuckFlavorViewSet(viewsets.ModelViewSet):
    queryset = DuckFlavor.objects.all()
    serializer_class = DuckFlavorSerializer

class FoodFlavorViewSet(viewsets.ModelViewSet):
    queryset = FoodFlavor.objects.all()
    serializer_class = FoodFlavorSerializer
