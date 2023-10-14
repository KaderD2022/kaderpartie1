from django.http import HttpResponseRedirect
from django.urls import reverse
from adminspace.models import Collaborateur, User
from django.core.exceptions import ObjectDoesNotExist


class Configuration:
    CLINIQUE_NAME = 'Clinique Longue vie'
    
    def current_user(request):
        try:
            user_id = request.session['id']
            collaborateur = Collaborateur.objects.get(user = User.objects.get(pk=user_id))
        except KeyError:
            return HttpResponseRedirect(reverse('adminspace:login'))
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('adminspace:login'))
        else:
            return collaborateur