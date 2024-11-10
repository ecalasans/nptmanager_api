from rest_framework import serializers

from main.hospital.models import Hospital
from main.medico.models import Medico

class MedicoSerializer(serializers.ModelSerializer):
    public_id = serializers.UUIDField(read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    hospitais = serializers.SlugRelatedField(
        many=True,
        slug_field='sigla',
        queryset=Hospital.objects.all(),
    )

    class Meta:
        model = Medico
        fields = ['public_id', 'username', 'first_name', 'last_name', 'email',
                  'crm', 'hospitais', 'created', 'updated', 'is_active',]