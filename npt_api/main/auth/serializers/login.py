from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import update_last_login
from main.medico.models import Medico
from main.medico.serializers import MedicoSerializer

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    user = MedicoSerializer(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),username=email, password=password)
            attrs['user'] = MedicoSerializer(user).data
        else:
            msg = _('Credenciais inválidas ou ausentes')
            raise serializers.ValidationError(msg, code='credenciais')

        return attrs

    def create(self, validated_data):
        user = validated_data['user']

        update_last_login(None, user)

        return {
            'user' : MedicoSerializer(user).data,
        }

