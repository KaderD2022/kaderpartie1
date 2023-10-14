from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from adminspace.models import Collaborateur, Service, User
from pharmaciestockspace.models import Produit, StockProduit
from receptionspace.models import Patient, Visite

from configuration import Configuration

# Create your views here.


    
def pharmacie_stock(request):
    collaborateur = Configuration.current_user(request)
    stocks = StockProduit.objects.all()
    produits = Produit.objects.all()

    context = {
        'collaborateur':collaborateur,
        'produits':produits, 
        'stocks':stocks, 

    }
    return render(request, 'pharmaciestockspace/stock.html', context)


def add_produit(request):
    collaborateur = Configuration.current_user(request)
    if request.method == 'POST':
        try:    
            name = request.POST['name']

        except KeyError:
            return HttpResponseRedirect(reverse('pharmaciestockspace:index'))
        else:
            Produit.objects.create(name = name, created_by=collaborateur)
            return HttpResponseRedirect(reverse('pharmaciestockspace:index'))
        

        
def add_stock(request):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    collaborateur = Configuration.current_user(request)
    try:   
        quantity = request.POST['quantity']
        print(quantity)
        price = request.POST['price']
        print(price)
        description = request.POST['description']
        print(description )
            # Récupérer l'objet Produit
        produit = Produit.objects.get(pk=request.POST['produit'])
                
            # Récupérer le nom du produit
        name = produit.name

    except:
        return HttpResponseRedirect(reverse('pharmaciestockspace:index'))
    else:
        StockProduit.objects.create(name =name, quantity = quantity, price = price, description = description, produit =produit, created_by=collaborateur)
        return HttpResponseRedirect(reverse('pharmaciestockspace:index'))       

def update_stock(request):
    if request.method == 'POST':
        try:
            stock = StockProduit.objects.get(pk=request.POST['stock'])
            stock.quantity = request.POST['quantity']
            stock.price = request.POST['price']
            stock.description = request.POST['description']
        except KeyError:
            return HttpResponseRedirect(reverse('pharmaciestockspace:index'))
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('pharmaciestockspace:index'))
        else:

            stock.save()
        finally:
            return HttpResponseRedirect(reverse('pharmaciestockspace:index'))
        
        
def delete_stock(request, id):
    stock = StockProduit.objects.get(pk=id)
    stock.delete()
    return HttpResponseRedirect(reverse('pharmaciestockspace:index'))