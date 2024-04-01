from django.contrib import admin
from .models import Proprietaire, Propriete

from django.contrib import admin
from .models import Proprietaire

class ProprietaireAdmin(admin.ModelAdmin):
    list_display = ['custom_user_username', 'custom_user_email', 'adresse']

    def custom_user_username(self, obj):
        return obj.custom_user.username
    custom_user_username.short_description = 'Username'
    
    def custom_user_email(self, obj):
        return obj.custom_user.email
    custom_user_email.short_description = 'Email'

admin.site.register(Proprietaire, ProprietaireAdmin)



@admin.register(Propriete)
class ProprieteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'adresse', 'prix', 'proprietaire', 'statut', 'type_propriete', 'nombre_chambres', 'nombre_salles_bains', 'surface_m2')
    list_filter = ('statut', 'type_propriete')
    search_fields = ('titre', 'adresse', 'prix', 'proprietaire__username', 'proprietaire__s_name')  # Utilisez 'proprietaire__username' au lieu de 'user'
    list_per_page = 20
