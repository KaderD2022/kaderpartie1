from django.db import models
    
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    state = models.CharField(max_length=5, default='on')
    token = models.CharField(max_length=255)

class Service(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Collaborateur(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

