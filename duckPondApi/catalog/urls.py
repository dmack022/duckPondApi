from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'ducks', views.DuckViewSet)
router.register(r'food', views.FoodViewSet)
router.register(r'flavors', views.FlavorViewSet)
router.register(r'duck-flavors', views.DuckFlavorViewSet)
router.register(r'food-flavors', views.FoodFlavorViewSet)
router.register(r'weather', views.WeatherViewSet)
router.register(r'water-temperatures', views.WaterTemperatureViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
