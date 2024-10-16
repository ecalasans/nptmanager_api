from rest_framework import generics

from main.hospital.models import Hospital
from main.hospital.serializers import HospitalSerializer


class HospitaisAPIView(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    lookup_field = 'public_id'  # Altera o campo de busca

class HospitalAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    lookup_field = 'public_id'