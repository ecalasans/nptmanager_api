from rest_framework import serializers
from main.hospital.models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['public_id', 'nome', 'sigla', 'is_active']