from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Proprietaire, Propriete, RecentActivity
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Proprietaire, RecentActivity,Contrat_bail

# Signal pour enregistrer une activité récente lorsqu'un Proprietaire est créé ou mis à jour
@receiver(post_save, sender=Proprietaire)
def log_proprietaire_activity(sender, instance, created, **kwargs):
    if created:
        action = 'Création du propriétaire'
    else:
        action = 'Mise à jour du propriétaire'
    RecentActivity.objects.create(proprietaire=instance, action=action)

# Signal pour enregistrer une activité récente lorsqu'un Proprietaire est supprimé
@receiver(post_delete, sender=Proprietaire)
def log_delete_proprietaire_activity(sender, instance, **kwargs):
    action = 'Suppression du propriétaire'
    RecentActivity.objects.create(proprietaire=instance, action=action)

@receiver(post_save, sender=Propriete)
def create_contrat_bail(sender, instance, created, **kwargs):
    if not created and instance.statut == 'indisponible':
        Contrat_bail.objects.create(propriete=instance)

# Signal pour enregistrer une activité récente lorsqu'une Propriete est créée ou mise à jour
@receiver(post_save, sender=Propriete)
def log_recent_activity(sender, instance, created, **kwargs):
    if created:
        action = 'Création de la propriété'
    else:
        action = 'Mise à jour de la propriété'
    RecentActivity.objects.create(proprietaire=instance.proprietaire, action=action)

# Signal pour enregistrer une activité récente lorsqu'une Propriete est supprimée
@receiver(post_delete, sender=Propriete)
def log_delete_activity(sender, instance, **kwargs):
    action = 'Suppression de la propriété'
    RecentActivity.objects.create(proprietaire=instance.proprietaire, action=action)