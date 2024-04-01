from django.db.models.signals import post_save
from django.dispatch import receiver
from main_apps.profiles.models import CustomUser
from main_apps.gestion.models import Proprietaire

@receiver(post_save, sender=Proprietaire)
def create_or_update_profile(sender, instance, created, **kwargs):
    
    """
    Crée un profile lorsque qu'un Proprietaire est créé.
    
    """
    if created:
        CustomUser.objects.create(user=instance)
    else:
        instance.customuser.save()

@receiver(post_save, sender=CustomUser)
def create_or_update_proprietaire(sender, instance, created, **kwargs):
    """
    Crée un Proprietaire lorsque qu'un profile est créé.
    """
    if created:
        Proprietaire.objects.create(username=instance.username)
    else:
        instance.proprietaire.save()
