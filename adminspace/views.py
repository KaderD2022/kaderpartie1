from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import check_password, make_password
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

import string

from adminspace.models import Collaborateur, Service, User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username, state = 'on')
            if check_password(password, user.password):
                collaborateur = Collaborateur.objects.get(user = user)
                request.session['id'] = user.id
                dashboard = collaborateur.service.name.lower()+'space:index'
                return HttpResponseRedirect(reverse(dashboard))
            else:
                context = {
                'message':'Nom d\'utilisateur ou mot de passe est incorrect'
                }
                return render(request, 'adminspace/login.html', context)
        except ObjectDoesNotExist:
            context = {
                'message':'Nom d\'utilisateur ou mot de passe est incorrect'
            }
            return render(request, 'adminspace/login.html', context)
    else:
        return render(request, 'adminspace/login.html')

def logout(request):
    del request.session['id']
    return HttpResponseRedirect(reverse('adminspace:login'))
   
def index(request):
    try:
        user_id = request.session['id']
        collaborateur = Collaborateur.objects.get(user = User.objects.get(pk=user_id))
        context = {
            'collaborateur':collaborateur,
        }
        
        return render(request, 'adminspace/index.html', context)
    except KeyError :
        context = {
            'message':'Veuillez vous connecter pour acceder à l\'application'
        }
        return HttpResponseRedirect(request, 'adminspace:login')
    
def collaborateurs(request):
    services = Service.objects.all()
    collaborateurs = Collaborateur.objects.all()
    context = {
        'services':services,
        'collaborateurs':collaborateurs
    }
    return render(request, 'adminspace/collaborateur.html', context)

def add_collaborateur(request):
    if request.method == 'POST':
        try:
            last_name = request.POST['last_name']
            first_name = request.POST['first_name']
            email = request.POST['email']
            phone = request.POST['phone']
            password = make_password(request.POST['password'], salt=None, hasher='default')
            service = Service.objects.get(pk=request.POST['service'])
        except KeyError:
            return HttpResponseRedirect(reverse('adminspace:collaborateurs'))
        else:
            user = User.objects.create(username = email, password = password, token = make_password(request.POST['email'], salt=None, hasher='default'))
            Collaborateur.objects.create(first_name = first_name, last_name = last_name, email = email, phone = phone, user = user, service = service)
        finally:
            return HttpResponseRedirect(reverse('adminspace:collaborateurs'))
        
def update_collaborateur(request):
    if request.method == 'POST':
        try:
            collaborateur = Collaborateur.objects.get(pk=request.POST['collaborateur'])
            user = collaborateur.user
            collaborateur.last_name = request.POST['last_name']
            collaborateur.first_name = request.POST['first_name']
            collaborateur.email = request.POST['email']
            collaborateur.phone = request.POST['phone']
            collaborateur.service = Service.objects.get(pk=request.POST['service'])
            if request.POST['password'] != '':
                user.password = make_password(request.POST['password'], salt=None, hasher='default')
        except KeyError:
            return HttpResponseRedirect(reverse('adminspace:collaborateurs'))
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('adminspace:collaborateurs'))
        else:
            user.save()
            collaborateur.save()
        finally:
            return HttpResponseRedirect(reverse('adminspace:collaborateurs'))
        
def delete_collaborateur(request, id):
    collaborateur = Collaborateur.objects.get(pk=id)
    user = collaborateur.user
    user.delete()
    collaborateur.delete()
    return HttpResponseRedirect(reverse('adminspace:collaborateurs'))

def suspend_on(request, id):
    user = User.objects.get(pk=id)
    user.suspend = 'on'
    user.save()

def suspend_off(request, id):
    user = User.objects.get(pk=id)
    user.suspend = 'off'
    user.save()