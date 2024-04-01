from django.shortcuts import redirect, render
from .models import Proprietaire,Propriete
from main_apps.gestion.forms import ProprieteForm,ProprietaireForm
from django.core.paginator import Paginator

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Proprietaire, Propriete
from main_apps.client.models import Client,Reservation
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import RecentActivity
from main_apps.profiles.models import CustomUser

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone

@login_required
def home(request):
    
    # Récupérer toutes les sessions actives
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())

    # Obtenir les IDs des utilisateurs connectés à partir des sessions actives
    user_ids = []

    for session in active_sessions:
        decoded_session = session.get_decoded()
        user_id = decoded_session.get('_profiles_customuser_id')
        if user_id:
            user_ids.append(int(user_id))

    # Récupérer les utilisateurs connectés en fonction de leurs IDs
    logged_in_users = CustomUser.objects.filter(id__in=user_ids)
    
    recent_activities = RecentActivity.objects.all().order_by('-timestamp')[:6] 
    proprietes = Propriete.objects.all()
    proprietaires = Proprietaire.objects.all()
    total_proprietaires = Proprietaire.objects.count()
    total_proprietes = Propriete.objects.count()
    total_client = Client.objects.count()
    total_reservation = Reservation.objects.count()

    paginator = Paginator(proprietaires, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Détermination du message de salutation en fonction de l'heure
    current_time = datetime.now()
    hour = current_time.hour
    greeting = "Bonjour" if 6 <= hour < 12 else "Bonsoir"

    context = {
        'logged_in_users': logged_in_users,
        'proprietes': proprietes,
        'proprietaires': page_obj,
        'total_proprietaires': total_proprietaires,
        'total_proprietes': total_proprietes,
        'page_obj': page_obj,
        'total_client': total_client,
        'total_reservation': total_reservation,
        'greeting': greeting,
        'recent_activities': recent_activities,
    }

    return render(request, 'gestion/home.html', context)

########################################################################################
from django.shortcuts import redirect, render
from .forms import ProprietaireForm
from .models import CustomUser, Proprietaire

@login_required
def ajouter_proprietaire(request):
    if request.method == "POST":
        form = ProprietaireForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            username = form.cleaned_data['username']
            s_name = form.cleaned_data['s_name']
            numero_telephone = form.cleaned_data['numero_telephone']
            adresse = form.cleaned_data['adresse']
            email = form.cleaned_data['email']
            
            #Vérifier si l'utilisateur personnalisé existe déjà
            custom_user, created = CustomUser.objects.get_or_create(email=email, defaults={
                'username': username,
                's_name': s_name,
                'numero_telephone': numero_telephone
            })

            # Créer le propriétaire associé au CustomUser
            proprietaire, created = Proprietaire.objects.get_or_create(custom_user=custom_user, adresse=adresse)
            return redirect('gestion:home')
    else:
        form = ProprietaireForm()

    context = {'form': form}
    return render(request, 'gestion/ajouter_proprietaire.html', context)

# ########################################################################################
# @login_required
# def ajouter_proprietaire(request):
#     if request.method == "POST":
#         form = ProprietaireForm(request.POST)
#         if form.is_valid():
#             # Récupérez les données du formulaire
#             username = form.cleaned_data['username']
#             s_name = form.cleaned_data['s_name']
#             numero_telephone = form.cleaned_data['numero_telephone']
#             adresse = form.cleaned_data['adresse']
#             email = form.cleaned_data['email']
            
#             # Vérifiez si l'utilisateur personnalisé existe déjà
#             custom_user, created = CustomUser.objects.get_or_create(email=email, defaults={
            
#                 'username': username,
#                 's_name': s_name,
#                 'numero_telephone': numero_telephone
#             })

#             # Créez le propriétaire associé au CustomUser
#             proprietaire, created = Proprietaire.objects.get_or_create(custom_user=custom_user, adresse=adresse)
#             return redirect('gestion:home')
#     else:
#         form = ProprietaireForm()

#     context = {'form': form}
#     return render(request, 'gestion/ajouter_proprietaire.html', context)

@login_required
def liste_proprietaires(request):
    
    proprietaires = Proprietaire.objects.all()
    
    context = {
        'proprietaires':proprietaires
    }
    
    return render(request, 'gestion/liste_proprietaires.html', context)     
        

################################### update # profile ####################################

from django.shortcuts import render, get_object_or_404
from .forms import ProprietaireForm
from .models import Proprietaire
@login_required
def update_proprietaire(request, proprietaire_id):
    proprietaire = get_object_or_404(Proprietaire, id=proprietaire_id)
    
    if request.method == 'POST':
        form = ProprietaireForm(request.POST, instance=proprietaire)
        if form.is_valid():
            form.save()
            return redirect('gestion:home')  # Rediriger vers la page d'accueil après la mise à jour
    else:
        form = ProprietaireForm()  # Remplir le formulaire avec les données existantes

    return render(request, 'gestion/update_proprietaire.html', context={'form': form})

@login_required
def supprimer_proprietaire(request, proprietaire_id):
    proprietaire = get_object_or_404(Proprietaire, id=proprietaire_id)
    
    if request.method == 'POST':
        proprietaire.delete()
        return redirect('gestion:home')  # Rediriger vers la page d'accueil après la suppression
    
    return render(request, 'gestion/supprimer_proprietaire.html', context={'proprietaire': proprietaire})

    

from django.shortcuts import render, redirect
from .forms import ProprieteForm
from .models import Propriete
@login_required
def ajouter_propriete(request):
    if request.method == 'POST':    
        form = ProprieteForm(request.POST)
        if form.is_valid():
            # Créez une nouvelle instance du modèle Propriete avec les données du formulaire        
            titre = form.cleaned_data['titre']
            adresse = form.cleaned_data['adresse']
            description = form.cleaned_data['description']
            prix = form.cleaned_data['prix']
            proprietaire = form.cleaned_data['proprietaire']
            statut = form.cleaned_data['statut']
            type_propriete = form.cleaned_data['type_propriete']
            nombre_chambres = form.cleaned_data['nombre_chambres']
            nombre_salles_bains = form.cleaned_data['nombre_salles_bains']
            surface_m2 = form.cleaned_data['surface_m2']

            # Enregistrez la nouvelle propriété dans la base de données
            try:
                propriete = Propriete.objects.create(
                    titre=titre,
                    adresse=adresse,
                    description=description,
                    prix=prix,
                    proprietaire=proprietaire,
                    statut=statut,
                    type_propriete=type_propriete,
                    nombre_chambres=nombre_chambres,
                    nombre_salles_bains=nombre_salles_bains,
                    surface_m2=surface_m2
                )
                return redirect('gestion:home')
            except Exception as e:
                print("Erreur lors de l'enregistrement de la propriété :", e)
                # Vous pouvez ajouter d'autres messages de débogage si nécessaire
        else:
            print("Formulaire invalide :", form.errors)
    else:
        form = ProprieteForm()

    context = {'form': form}
    return render(request, 'gestion/ajouter_propriete.html', context)
################################ Update propriete ##################################################################
@login_required
def update_propriete(request, propriete_id):
    propriete = get_object_or_404(Propriete, id=propriete_id)
    
    if request.method == 'POST':
        form = ProprieteForm(request.POST, instance=propriete)
        if form.is_valid():
            form.save()
            return redirect('gestion:home')  # Rediriger vers la page d'accueil après la mise à jour
    else:
        form = ProprieteForm()  # Remplir le formulaire avec les données existantes

    return render(request, 'gestion/update_propriete.html', context={'form': form})
@login_required
def supprimer_propriete(request, propriete_id):
    propriete = get_object_or_404(Propriete, id=propriete_id)
    
    if request.method == 'POST':
        propriete.delete()
        return redirect('gestion:home')  # Rediriger vers la page d'accueil après la suppression
    
    return render(request, 'gestion/supprimer_propriete.html', context={'propriete': propriete})

@login_required
def details_list(request, propriete_id):
    propriete = get_object_or_404(Propriete, id=propriete_id)
    return render(request, 'gestion/details_list.html', {'propriete': propriete})
@login_required
def list_users(request):
    return render(request,'gestion/list_users.html')