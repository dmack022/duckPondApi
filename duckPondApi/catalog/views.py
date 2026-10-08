from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Duck, Food, Flavor, DuckFlavor, FoodFlavor, WaterTemperature, Weather
from .serializers import DuckSerializer, FoodSerializer, FlavorSerializer, DuckFlavorSerializer, FoodFlavorSerializer, WaterTemperatureSerializer, WeatherSerializer

class DuckViewSet(viewsets.ModelViewSet):
    queryset = Duck.objects.all()
    serializer_class = DuckSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FlavorViewSet(viewsets.ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class WaterTemperatureViewSet(viewsets.ModelViewSet):
    queryset = WaterTemperature.objects.all()
    serializer_class = WaterTemperatureSerializer

# Relationship ViewSets

class DuckFlavorViewSet(viewsets.ModelViewSet):
    queryset = DuckFlavor.objects.all()
    serializer_class = DuckFlavorSerializer

class FoodFlavorViewSet(viewsets.ModelViewSet):
    queryset = FoodFlavor.objects.all()
    serializer_class = FoodFlavorSerializer
