from django.urls import path
from . import views

urlpatterns = [
    path("ducks/", views.DucksListCreate.as_view(), name="ducks-view-create")
]
