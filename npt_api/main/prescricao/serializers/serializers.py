import uuid

from rest_framework import serializers

from main.prescricao.models import Prescricao

class PrescricaoSerializer(serializers.ModelSerializer):
    public_id = serializers.UUIDField(read_only=True, format='hex')
    data = serializers.DateTimeField(read_only=True, format='%d/%m/%Y hh:mm:ss')

    class Meta:
        model = Prescricao
        fields = '__all__'

