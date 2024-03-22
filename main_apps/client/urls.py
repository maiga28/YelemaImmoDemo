from django.urls import path
from . import views
  
app_name = 'client'  

urlpatterns = [
    
    path('', views.list_client, name='client'),
    path('ajouter_client/', views.ajouter_client, name='ajouter_client'),
    path('reservation/<int:propriete_id>/', views.reservation, name='reservation'),
    path('update_client/<int:client_id>/',views.update_client, name='update_client' ),
    path('liste_reservation/', views.liste_reservation, name='liste_reservation')
    # Ajoutez d'autres modèles d'URL au besoin
]
