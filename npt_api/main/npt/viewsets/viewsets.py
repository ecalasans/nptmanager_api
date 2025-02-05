from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from main.npt.models import Npt
from main.npt.serializers import NptSerializer

class NptViewSet(viewsets.ModelViewSet):
    serializer_class = NptSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        return Npt.objects.all()

    def get_object(self):
        obj = Npt.objects.get_obje(pk=self.kwargs['pk'])

        self.check_object_permissions(self.request, obj)

        return obj