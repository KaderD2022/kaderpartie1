from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from adminspace.models import Collaborateur, Service, User
from receptionspace.models import Patient, Visite

from configuration import Configuration


    
def patients(request):
    collaborateur = Configuration.current_user(request)
    patients = Patient.objects.all()
    services = Service.objects.exclude(name__in=['Admin', 'Pharmacie', 'Caisse', 'Reception'])
    context = {
        'collaborateur':collaborateur,
        'patients':patients, 
        'services':services
    }
    return render(request, 'receptionspace/patient.html', context)

def add_patient(request):
    collaborateur = Configuration.current_user(request)
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            sexe = request.POST['sexe']
            habitation = request.POST['habitation']
            birthday = request.POST['birthday']
        except KeyError:
            return HttpResponseRedirect(reverse('receptionspace:index'))
        else:
            Patient.objects.create(first_name = first_name, last_name = last_name, email = email, phone = phone, sexe = sexe, habitation = habitation, birthday = birthday, created_by=collaborateur)
            return HttpResponseRedirect(reverse('receptionspace:index'))

def rdvs(request):
    collaborateur = Configuration.current_user(request)
    context = {
        'collaborateur':collaborateur,
    }
    return render(request, 'receptionspace/rdvs.html', context)
        
def add_visite(request, id_patient):
    collaborateur = Configuration.current_user(request)
    try:
        # Sélection du patient 
        patient = Patient.objects.get(pk=id_patient)
        #Initialisation des données du formulaire
        service = Service.objects.get(pk=request.POST['service'])
        taille = request.POST['taille']
        masse = request.POST['masse']
        temperature = request.POST['temperature']
        motifs = request.POST['motifs']
    except:
        return HttpResponseRedirect(reverse('receptionspace:index'))
    else:
        patient.visite_set.create(taille = taille, masse = masse, temperature = temperature, motifs = motifs, service=service, created_by = collaborateur)
        return HttpResponseRedirect(reverse('receptionspace:patients'))