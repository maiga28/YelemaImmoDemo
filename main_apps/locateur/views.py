from django.shortcuts import render,redirect
from .forms import LocateurForm
from . models import Locateur
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def gestion_locateur(request):
    locateurs = Locateur.objects.all()
    
    return render(request,'locateur/gestion_locateur.html', context ={'locateurs':locateurs})

def lien_conf(request):
    
    return render(request,'locateur/lien_conf.html')

@login_required
def ajouter_locateur(request):
    if request.method == 'POST':
        form = LocateurForm()
        if form.is_valid():
            
            name = form.cleaned_data['name']
            prenom = form.cleaned_data['prenom']
            tell = form.cleaned_data['tell']
            statut = form.cleaned_data['statut']
            email = form.cleaned_data['email']
            
            locateur, created = Locateur.objects.get_or_create(
                email=email,
                defaults={
                    'name': name,
                    'prenom': prenom,
                    'tell': tell,
                    'statut': statut,
                    'email': email,
                })
            locateur = authenticate(username=email)
            if locateur is not None:
                login(request, locateur)

            msg = 'User created successfully.'
            success = True
            return redirect('locateur:gestion_locateur')
    else:
        form = LocateurForm()

    return render(request, 'locateur/ajouter_locateur.html', {'form': form, 'msg': msg, 'success': success})
            
            
            