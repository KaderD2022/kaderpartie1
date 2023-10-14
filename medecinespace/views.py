from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse

from receptionspace.models import Patient, Visite
from .models import Antecedant, DonneeAdministrative

from configuration import Configuration

def visites(request, id_patient):
    collaborateur = Configuration.current_user(request)
    try:
        # Sélection du patient 
        patient = Patient.objects.get(pk=id_patient)
    except:
        return HttpResponseRedirect(reverse('medecinespace:index'))
    else:
        visites = patient.visite_set.all().order_by('-date_time')
        context = {
            'collaborateur':collaborateur,
            'visites':visites
        }
        return render(request, 'medecinespace/consultations.html', context)

def file_visites(request):
    collaborateur = Configuration.current_user(request)
    visites = Visite.objects.all().order_by('-date_time')
    context = {
        'collaborateur':collaborateur,
        'visites':visites
    }
    return render(request, 'medecinespace/attente.html', context)

def patients(request):
    collaborateur = Configuration.current_user(request)
    patients = Patient.objects.all()
    context = {
        'collaborateur':collaborateur,
        'patients':patients
    }
    return render(request, 'medecinespace/patient.html', context)

def add_detail_visite(request, id_visite):
    collaborateur = Configuration.current_user(request)
    try:
        # Sélection de la visite
        visite = Visite.objects.get(pk=id_visite)
        # Sélection du patient 
        patient = visite.patient
    except:
        return HttpResponseRedirect(reverse('receptionspace:index'))
    else:
        context = {
            'collaborateur':collaborateur,
            'patient':patient,
            'visite':visite,
        }
        return render(request, 'medecinespace/detail_visite.html', context)
    
def add_donnee_administrative(request, id_visite):
    Configuration.current_user(request)
    if request.method == 'POST':
        try:
            # Sélection de la visite
            visite = Visite.objects.get(pk=id_visite)
            # Données du formulaire
            school = request.POST['school']
            conjugal_status = request.POST['conjugal_status']
            type_populate = request.POST['type_populate']
            social_protection = request.POST['social_protection']
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('medecinespace:index'))
        except KeyError:
            return HttpResponseRedirect(reverse('medecinespace:add-detail', args=[visite.id]))
        else:
            DonneeAdministrative.objects.create(school = school, conjugal_status = conjugal_status, type_populate = type_populate, social_protection = social_protection, visite = visite)
            return HttpResponseRedirect(reverse('medecinespace:add-detail', args=[visite.id]))
        
def add_antecedant(request, id_visite):
    if request.method == 'POST':
        try:
            # Sélection de la visite
            visite = Visite.objects.get(pk=id_visite)
            # Données du formulaire
            anterieur_traitement = request.POST['anterieur_traitement']
            ddr = request.POST['ddr']
            hta = request.POST['hta']
            current_pregment = request.POST['current_pregment']
            diabete = request.POST['diabete']
            tabac = request.POST['tabac']
            alchool = request.POST['alchool']
            other = request.POST['other']
            visit_type = request.POST['visit_type']
            chirugical = request.POST['chirugical']
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('medecinespace:index'))
        except KeyError:
            return HttpResponseRedirect(reverse('medecinespace:add-detail', args=[visite.id]))
        else:
            Antecedant.objects.create(anterieur_traitement = anterieur_traitement, hta = hta, current_pregment = current_pregment, diabete =diabete, tabac = tabac, alchool = alchool, other = other, visit_type = visit_type, churigical = chirugical, visite = visite)
            return HttpResponseRedirect(reverse('medecinespace:add-detail', args=[visite.id]))