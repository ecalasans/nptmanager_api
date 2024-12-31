from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from main.hospital.models import Hospital
from main.hospital.serializers import HospitalSerializer

from main.paciente.models import Paciente
from main.paciente.serializers import PacienteSerializer

from django.shortcuts import get_object_or_404

class HospitalViewSet(ModelViewSet):
    serializer_class = HospitalSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get_queryset(self):
        return Hospital.objects.filter(is_active=True)

    @action(detail=False, methods=['get'], url_path=r'(?P<sigla>[^/.]+)/pacientes')
    def pacientes(self, request, sigla=None):
        hospital = get_object_or_404(Hospital, sigla=sigla)
        pacientes = Paciente.objects.filter(cod_hospital=hospital).order_by("cod_leito")
        serializer  = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)