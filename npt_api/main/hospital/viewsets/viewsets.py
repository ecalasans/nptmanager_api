from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from main.hospital.models import Hospital
from main.hospital.serializers import HospitalSerializer

class HospitalViewSet(ModelViewSet):
    serializer_class = HospitalSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def get_queryset(self):
        return Hospital.objects.all()