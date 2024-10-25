from rest_framework.routers import SimpleRouter

from main.medico.viewsets import MedicoViewSet
from main.auth.viewsets import RegisterViewSet

router = SimpleRouter()

router.register(r'medicos', MedicoViewSet, basename='medico')
router.register(r'auth/register', RegisterViewSet, basename='register')

urlpatterns = [
    *router.urls
]