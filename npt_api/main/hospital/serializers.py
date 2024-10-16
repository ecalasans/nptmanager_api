from rest_framework import serializers

from main.hospital.models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True,
                               source='public_id')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Hospital
        fields = ('id', 'name', 'sigla', 'created', 'updated')
