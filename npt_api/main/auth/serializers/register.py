from rest_framework import serializers

from main.medico.models import Medico
from main.medico.serializers import MedicoSerializer
from main.hospital.models import Hospital

class RegisterSerializer(MedicoSerializer):
    password = serializers.CharField(
        min_length=8,
        max_length=128,
        write_only=True,
        required=True,
    )
    crm = serializers.CharField(write_only=True)
    hospitais = serializers.SlugRelatedField(
        many=True,
        slug_field='sigla',
        queryset=Hospital.objects.all(),
    )
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Medico
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password',
                  'crm', 'hospitais', 'created', 'updated', 'is_active',]


    def create(self, validated_data):
        hospitais_data = validated_data.pop('hospitais', None) # Retira 'hospitais' da criação do registro

        medico = Medico.objects.create_user(**validated_data) # Cria o médico sem os hospitais

        #  Se houver hospitais adiciona ao médico
        if hospitais_data:
            hospitais = Hospital.objects.filter(sigla__in=hospitais_data)
            medico.hospitais.set(hospitais_data)

        medico.save()  # Assegura que o registro será salvo

        return medico