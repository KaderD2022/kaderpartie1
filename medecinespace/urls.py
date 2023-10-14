from django.urls import path
from . import views

app_name = 'medecinespace'

urlpatterns = [
    path('', views.file_visites, name='index'),
    path('patients/', views.patients, name='patients'),
    path('visites/<int:id_patient>', views.visites, name='visites'),
    path('add-detail/<int:id_visite>', views.add_detail_visite, name='add-detail'),
    path('add-donnee-administrative/<int:id_visite>', views.add_donnee_administrative, name='add-donnee-administrative'),
    path('add-antecedant/<int:id_visite>', views.add_antecedant, name='add-antecedant'),
]
