from django.db import models

from receptionspace.models import Visite

class DonneeAdministrative(models.Model):
    school = models.CharField(max_length=3, null=True)
    conjugal_status = models.CharField(max_length=15, null=True)
    type_populate = models.CharField(max_length=255, null=True)
    social_protection = models.CharField(max_length=255, null=True)
    visite = models.OneToOneField(Visite, on_delete=models.CASCADE)

class Antecedant(models.Model):
    anterieur_traitement = models.CharField(max_length=255, null=True)
    ddr = models.DateField(null=True)
    hta = models.CharField(max_length=255, null=True)
    current_pregment = models.CharField(max_length=255, null=True)
    diabete = models.CharField(max_length=255, null=True)
    tabac = models.CharField(max_length=255, null=True)
    alchool = models.CharField(max_length=255, null=True)
    other = models.CharField(max_length=255, null=True)
    visit_type = models.CharField(max_length=255, null=True)
    churigical = models.CharField(max_length=255, null=True)
    visite = models.OneToOneField(Visite, on_delete=models.CASCADE)

class ExamenClinique(models.Model):
    frequence_respiratoire = models.IntegerField(null=True)
    zscrore = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ta = models.CharField(max_length=7, null=True)
    pouls = models.IntegerField(null=True)
    perimetre_cranien = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    perimetre_branchial = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    tuberculose = models.CharField(max_length=5, null=True)
    examen_clinique = models.CharField(max_length=255, null=True)
    diagnostique_retenu = models.CharField(max_length=255)
    autre_pathologie = models.CharField(max_length=255)

class ExamenComplementaire(models.Model):
    tdr_paludisme = models.CharField(max_length=255, null=True)
    goutte_epaisse = models.CharField(max_length=255, null=True)
    milda_12_a_59 = models.CharField(max_length=255, null=True)
    remise_milda_12_a_59 = models.CharField(max_length=255, null=True)
    cdip_propose = models.CharField(max_length=5, null=True)
    cdip_realise = models.CharField(max_length=5, null=True)
    code_depistage = models.CharField(max_length=255, null=True)
    glycemie_a_jeun = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    glycemie_non_a_jeun = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    autre_examen = models.CharField(max_length=255, null=True)