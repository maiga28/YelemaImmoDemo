from django.shortcuts import render
from main_apps.client.models import Client,Reservation
from main_apps.gestion.models import Proprietaire,Propriete
from django.views.decorators.http import require_http_methods
# from main_apps.account.models import Admiuser

def index(request):
    proprietes = Propriete.objects.all()
    proprietaires = Proprietaire.objects.all()
    context = {
        'proprietes':proprietes,
        'proprietaires':proprietaires
    }
    return render(request, 'index.html',context)

@require_http_methods(['POST'])
def search(request):
    search = request.POST.get('search', '')
    
    if len(search) == 0:
        return render(request, 'propriete.html', {'Propriete': []})
    
    propriete_objects = Propriete.objects.filter(titre__icontains=search)
    
    return render(request, 'gestion/propriete.html', {'Propriete': propriete_objects})

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def connexion(request):
    return render(request, 'about.html')

from django.test import SimpleTestCase, override_settings

def custom_page_not_found(request, unknown_path):
    return render(request, 'gestion/404.html', {'unknown_path': unknown_path}, status=404)