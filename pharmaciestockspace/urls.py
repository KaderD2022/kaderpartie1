from django.contrib import admin
from django.urls import include, path

from pharmaciestockspace import views

app_name = 'pharmaciestockspace'

urlpatterns = [
    path('', views.pharmacie_stock, name='index'),
    path('add_produit/', views.add_produit, name='add_produit'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('delete_stock/<int:id>', views.delete_stock, name='delete_stock'),
    path('update_stock/', views.update_stock, name='update_stock'),
    # path('add-detail/<int:id_visite>', views.add_detail_visite, name='add-detail'),
    # path('add-donnee-administrative/<int:id_visite>', views.add_donnee_administrative, name='add-donnee-administrative'),
    # path('add-antecedant/<int:id_visite>', views.add_antecedant, name='add-antecedant'),
]
