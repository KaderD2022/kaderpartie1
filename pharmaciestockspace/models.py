from django.db import models

from django.db import models
from adminspace.models import Collaborateur
# Create your models here.

class Produit(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Collaborateur, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)
    
class StockProduit(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(Collaborateur, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)    
    
    
    