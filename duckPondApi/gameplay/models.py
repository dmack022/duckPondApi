from django.db import models
# from catalog.models import Food, WaterTemperature

# Create your models here.
class Pond(models.Model):
    pond_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    weather_id = models.IntegerField()
    # description = models.CharField(max_length=500)

    class Meta:
        db_table = "pond"
        verbose_name = "Pond"
        verbose_name_plural = "Ponds"

    def __str__(self):
        return f"{self.name}"
    
class PondSection(models.Model):
    pond_section_id = models.AutoField(primary_key=True)
    pond_id = models.ForeignKey(Pond, on_delete=models.RESTRICT)

    class Meta:
        db_table = "pond_section"
        verbose_name = "Pond Section"
        verbose_name_plural = "Pond Sections"

    def __str__(self):
        return f"{self.name}"

    
class SpawnPoint(models.Model):
    spawn_point_id = models.AutoField(primary_key=True)
    pond_section_id = models.ForeignKey(PondSection, on_delete=models.RESTRICT)
    duck = models.ForeignKey(
        "catalog.Duck", on_delete=models.SET_NULL, null=True, blank=True, related_name="spawn_points"
    )

    class Meta:
        db_table = "spawn_point"
        verbose_name = "Spawn Point"
        verbose_name_plural = "Spawn Points"

    def __str__(self):
        return f"{self.name}"
    
#Relationship Tables

class SpawnPointFood(models.Model):
    spawn_point = models.ForeignKey("gameplay.SpawnPoint", on_delete=models.CASCADE, related_name="filled_spawn_point")
    food = models.ForeignKey("catalog.Food", on_delete=models.CASCADE, related_name="food")
    time_placed = models.DateTimeField()

    class Meta:
        db_table = "spawn_point_food"  # Explicit table name
        constraints = [
            models.UniqueConstraint(
                fields=["spawn_point", "food"], name="unique_spawn_point_food"
            )
        ]

