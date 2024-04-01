from django.urls import path
from .views import profile_view,edit_profile,delete_profile,create_profile

app_name = 'profiles'

urlpatterns = [
    # Vue pour afficher le profil utilisateur
    path('<int:user_id>/', profile_view, name='profile_view'),

    # Vue pour modifier le profil utilisateur
    path('edit/', edit_profile, name='edit_profile'),

    # Vue pour supprimer le profil utilisateur
    path('delete/', delete_profile, name='delete_profile'),

    # Vue pour créer un nouveau profil utilisateur
    path('create/', create_profile, name='create_profile'),
]
