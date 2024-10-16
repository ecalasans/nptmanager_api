from rest_framework import generics

from main.user.models import Medico
from main.user.serializers import MedicoSerializer

class MedicosAPIView(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class MedicoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer