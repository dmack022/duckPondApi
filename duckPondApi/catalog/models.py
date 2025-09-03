from django.db import models
# from gameplay.models import SpawnPoint, PondSection

# Create your models here.
class Flavor(models.Model):
    flavor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    # description = models.CharField(max_length=500)

    class Meta:
        db_table = "flavor"
        verbose_name = "Flavor"
        verbose_name_plural = "Flavors"

    def __str__(self):
        return f"{self.name}"


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    # description = models.CharField(max_length=500)

    flavors = models.ManyToManyField(Flavor, through="FoodFlavor")

    class Meta:
        db_table = "food"
        verbose_name = "Food"
        verbose_name_plural = "Foods"

    def __str__(self):
        return f"{self.name}"
    
    

class Toy(models.Model):
    toy_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    pond_section = models.ForeignKey("gameplay.PondSection", on_delete=models.RESTRICT)
    # description = models.CharField(max_length=500)

    class Meta:
        db_table = "toy"
        verbose_name = "Toy"
        verbose_name_plural = "Toys"

    def __str__(self):
        return f"{self.name}"
    

class Weather(models.Model):
    weather_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    # description = models.CharField(max_length=500)

    class Meta:
        db_table = "weather"
        verbose_name = "Weather"
        verbose_name_plural = "Weathers"

    def __str__(self):
        return f"{self.name}"
    

class WaterTemperature(models.Model):
    temp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    pond_section = models.ManyToManyField("gameplay.PondSection")
    # description = models.CharField(max_length=500)

    class Meta:
        db_table = "water_temperature"
        verbose_name = "Water Temperature"
        verbose_name_plural = "Water Temperatures"

    def __str__(self):
        return f"{self.name}"
    

class Duck(models.Model):
    duck_id = models.AutoField(primary_key=True)  # Auto-increment int
    name = models.CharField(max_length=50, unique=True)  # Must be unique
    rarity = models.IntegerField()
    favorite_food = models.CharField(max_length=100)
    # biography = models.CharField(max_length=500)
    duck_energy = models.IntegerField()

    spawn_point = models.ForeignKey("gameplay.SpawnPoint", on_delete=models.RESTRICT)

    flavors = models.ManyToManyField(Flavor, through="DuckFlavor")
    water_temp = models.ManyToManyField(WaterTemperature, through="DuckWaterTemp")
    weather = models.ManyToManyField(Weather, through="DuckWeather")
    toy = models.ManyToManyField(Toy, through="DuckToy")

    class Meta:
        db_table = "ducks"  # Explicit table name
        verbose_name = "Duck"
        verbose_name_plural = "Ducks"

    def __str__(self):
        return f"{self.name} (Rarity: {self.rarity})"

# Relationship Models

class DuckFlavor(models.Model):
    duck = models.ForeignKey(Duck, on_delete=models.CASCADE, related_name="flavor_preferences")
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE, related_name="ducks")
    preference_value = models.IntegerField()

    class Meta:
        db_table = "duck_flavor"  # Explicit table name
        constraints = [
            models.UniqueConstraint(
                fields=["duck", "flavor"], name="unique_duck_flavor"
            )
        ]


class DuckWaterTemp(models.Model):
    duck = models.ForeignKey(Duck, on_delete=models.CASCADE, related_name="water_temp_preferences")
    water_temp = models.ForeignKey(WaterTemperature, on_delete=models.CASCADE, related_name="ducks")
    preference_value = models.IntegerField()

    class Meta:
        db_table = "duck_water_temp"  # Explicit table name
        constraints = [
            models.UniqueConstraint(
                fields=["duck", "water_temp"], name="unique_duck_water_temp"
            )
        ]


class DuckWeather(models.Model):
    duck = models.ForeignKey(Duck, on_delete=models.CASCADE, related_name="weather_preferences")
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE, related_name="ducks")
    preference_value = models.IntegerField()

    class Meta:
        db_table = "duck_weather"  # Explicit table name
        constraints = [
            models.UniqueConstraint(
                fields=["duck", "weather"], name="unique_duck_weather"
            )
        ]

class DuckToy(models.Model):
    duck = models.ForeignKey(Duck, on_delete=models.CASCADE, related_name="toy_preferences")
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE, related_name="ducks")
    preference_value = models.IntegerField()

    class Meta:
        db_table = "duck_toy"  # Explicit table name
        constraints = [
            models.UniqueConstraint(
                fields=["duck", "toy"], name="unique_duck_toy"
            )
        ]


class FoodFlavor(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="foods")
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE, related_name="flavors")
    strength = models.IntegerField()

    class Meta:
        db_table = "food_flavor"  # Explicit table name
        constraints = [
            models.UniqueConstraint(
                fields=["food", "flavor"], name="unique_food_flavor"
            )
        ]