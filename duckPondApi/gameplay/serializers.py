from django.db import transaction
from rest_framework import serializers
from .models import Pond, PondSection

class PondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pond
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        pond = super().create(validated_data)
        for _ in range(2):
            PondSection.objects.create(pond_id=pond)
        return pond
