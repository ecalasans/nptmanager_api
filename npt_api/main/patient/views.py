from rest_framework import generics

from main.patient.models import Paciente
from main.patient.serializers import PacienteSerializer

class PatientsAPIView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class PatientAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = 'public_id'