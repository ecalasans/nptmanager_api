from django.urls import path, include
from main.hospital.views import HospitalAPIView, HospitaisAPIView
from main.patient.views import PatientsAPIView, PatientAPIView
from main.user.views import MedicoAPIView, MedicosAPIView

urlpatterns = [
    path('hospitais/', HospitaisAPIView.as_view(), name='hospitais'),
    path('medicos/', MedicosAPIView.as_view(), name='medicos'),
    path('medicos/<str:public_id>/', MedicoAPIView.as_view(), name='medico'),
    path('hospitais/<str:public_id>/', HospitalAPIView.as_view(), name='hospital'),
    path('pacientes/', PatientsAPIView.as_view(), name='pacientes'),
    path('pacientes/<str:public_id>/', PatientAPIView.as_view(), name='paciente'),
]