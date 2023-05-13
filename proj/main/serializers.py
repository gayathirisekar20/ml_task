from rest_framework import serializers
from .models import Cereal

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cereal
        fields='__all__'