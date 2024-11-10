from rest_framework.routers import SimpleRouter

from main.auth.viewsets import LoginViewSet, RefreshViewSet, RegisterViewSet
from main.medico.viewsets import MedicoViewSet
from main.hospital.viewsets import HospitalViewSet

router = SimpleRouter()

router.register(r'medicos', MedicoViewSet, basename='medicos')
router.register(r'hospitais', HospitalViewSet, basename='hospitais')
router.register(r'auth/register', RegisterViewSet, basename='register')
router.register(r'auth/login', LoginViewSet, basename='login')
router.register(r'auth/refresh', RefreshViewSet, basename='refresh')

urlpatterns = [
    *router.urls
]