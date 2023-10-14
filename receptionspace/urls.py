from django.urls import path
from . import views

app_name = 'receptionspace'

urlpatterns = [
    path('', views.rdvs, name='index'),
    path('patients/', views.patients, name='patients'),
    path('add-patient/', views.add_patient, name='add-patient'),
    path('add-visite/<int:id_patient>', views.add_visite, name='add-visite'),
]
