from rest_framework import serializers
from .models import Duck, Flavor, Food, Toy, Weather, WaterTemperature, FoodFlavor, DuckToy, DuckWeather, DuckWaterTemp, DuckFlavor

class DuckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duck
        fields = ["duck_id", "name", "rarity", "favorite_food", "duck_energy"]

class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ["flavor_id", "name"]

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ["food_id", "name"]

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ["toy_id", "name"]

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ["weather_id", "name"]

class WaterTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterTemperature
        fields = ["temp_id", "name"]


# Relationship Tables

class DuckFlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuckFlavor
        fields = ["duck", "flavor", "preference_value"]


class DuckWaterTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuckWaterTemp
        fields = ["duck", "water_temp", "preference_value"]


class DuckWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuckWeather
        fields = ["duck", "weather", "preference_value"]


class DuckToySerializer(serializers.ModelSerializer):
    class Meta:
        model = DuckToy
        fields = ["duck", "toy", "preference_value"]


class FoodFlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodFlavor
        fields = ["food", "flavor", "preference_value"]