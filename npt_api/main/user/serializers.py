from rest_framework import serializers

from main.hospital.models import Hospital
from main.user.models import Medico

class MedicoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id',
                               read_only=True,
                               format='hex')
    email = serializers.EmailField(write_only=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    hospitais = serializers.SlugRelatedField(many=True,
                                             slug_field='public_id',
                                             queryset=Hospital.objects.all())

    class Meta:
        model = Medico
        fields = ['id', 'username', 'first_name', 'last_name', 'crm',
                  'email', 'hospitais','is_active', 'created', 'updated']

