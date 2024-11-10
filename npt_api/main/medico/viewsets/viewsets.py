from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from main.medico.models import Medico
from main.medico.serializers import MedicoSerializer

class MedicoViewSet(ModelViewSet):
    serializer_class = MedicoSerializer
    permission_classes = [AllowAny]
    methods = ('GET', 'POST', 'PATCH', 'PUT')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Medico.objects.all()

        return Medico.objects.exclude(is_superuser=True)

    def get_object(self):
        obj = Medico.objects.get_object_by_public_id(pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)

        return obj