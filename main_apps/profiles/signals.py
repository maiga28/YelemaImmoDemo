from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, m2m_changed, pre_init, post_init
from django.dispatch import receiver
from django.core.signals import request_started, request_finished, got_request_exception, setting_changed
from django.contrib.auth.models import Group
from .models import CustomUser, RecentActivity
from django.contrib.auth.models import User
      
@receiver(post_save, sender=CustomUser)
def create_customer_profile(sender, instance, created, **kwargs):
    
    if created:
        action = "Creation d'un nouveau profile"
    else:
        action = 'Mise à jour du propriétaire'
    RecentActivity.objects.create(custom_user=instance, action=action)

@receiver(post_delete, sender=RecentActivity)
def delete_customer_profile(sender, instance, **kwargs):
    instance.custom_user.delete()

@receiver(pre_save, sender=CustomUser)
def custom_user_pre_save(sender, instance, **kwargs):
    # Ajoutez ici le code pour effectuer des actions avant que l'instance ne soit sauvegardée
    print("CustomUser pre_save signal triggered.")
    print("Instance:", instance)

# pre_delete signal
@receiver(pre_delete, sender=CustomUser)
def custom_user_pre_delete(sender, instance, **kwargs):
    RecentActivity.objects.get(CustomUser_id =instance).delete()
