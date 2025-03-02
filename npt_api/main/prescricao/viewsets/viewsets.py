from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_datetime

from main.prescricao.models import Prescricao
from main.prescricao.serializers import PrescricaoSerializer

class PrescricaoViewSet(viewsets.ModelViewSet):
    serializer_class = PrescricaoSerializer
    http_method_names = ['get', 'post', 'update', 'patch', 'delete']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Prescricao.objects.all()

        # Captura os parâmetros da requisição
        presc_data = self.request.GET.get('data', None)
        presc_paciente_id = self.request.GET.get('public_id', None)

        # Se existirem os parâmetros faz o filtro;  senão retorna todos os objetos
        if presc_paciente_id:
            queryset = queryset.filter(cod_npt__cod_pac__public_id=presc_paciente_id)

        if presc_data:
            # Converte para o formato de data aceitável para pesquisa
            data_obj = parse_datetime(presc_data)

            if data_obj:
                queryset = queryset.filter(data=data_obj)

        return queryset


    def get_object(self):
        obj = Prescricao.objects.get_object_by_public_id(pk=self.kwargs['public_id'])

        self.check_object_permissions(self.request, obj)

        return obj