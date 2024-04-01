from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, m2m_changed, pre_init, post_init
from django.dispatch import receiver
from django.core.signals import request_started, request_finished, got_request_exception, setting_changed
from django.contrib.auth.models import Group
from .models import CustomUser, RecentActivity
from django.contrib.auth.models import User
      
@receiver(post_save, sender=CustomUser)
def create_customer_profile(sender, instance, created, **kwargs):
    
    if created:
        # Ajouter une activité récente pour indiquer la création d'un nouvel utilisateur
        print (f"User {instance.id} created")
    else:
        # Ajouter une activité récente pour indiquer la mise à jour d'un utilisateur existant
            # Ajoutez ici le code pour effectuer des actions avant que l'instance ne soit sauvegardée
        print("CustomUser pre_save signal triggered.")
        print("Instance:", instance)

@receiver(post_delete, sender=CustomUser)
def delete_customer_profile(sender, instance, **kwargs):
    instance.user.delete()

@receiver(pre_save, sender=CustomUser)
def custom_user_pre_save(sender, instance, **kwargs):
    # Ajoutez ici le code pour effectuer des actions avant que l'instance ne soit sauvegardée
    print("CustomUser pre_save signal triggered.")
    print("Instance:", instance)

# pre_delete signal
@receiver(pre_delete, sender=CustomUser)
def custom_user_pre_delete(sender, instance, **kwargs):
    RecentActivity.objects.filter(CustomUser=instance).delete()
    
# post_delete signal
@receiver(post_delete, sender=CustomUser)
def custom_user_post_delete(sender, instance, **kwargs):
    # Code to execute after deleting a CustomUser instance
    print(f"L'utilisateur {instance.username} a été supprimé avec succès.")