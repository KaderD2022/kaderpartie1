from django.db import models

from adminspace.models import Collaborateur, Service

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sexe = models.CharField(max_length=1, default=None)
    birthday = models.DateField()
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=10)
    habitation = models.CharField(max_length=255)
    created_by = models.ForeignKey(Collaborateur, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)

class Visite(models.Model):
    taille = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    masse = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    temperature = models.DecimalField( max_digits=3, decimal_places=1, null=True)
    motifs = models.TextField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Collaborateur, on_delete=models.SET_NULL, null=True)
