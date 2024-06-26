from django.db import models
from main_apps.gestion.models import Propriete
from main_apps.profiles.models import CustomUser


# Create your models here.
class Client(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='image/')
    tell = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Reservation(models.Model):
    propriete = models.ForeignKey(Propriete, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)