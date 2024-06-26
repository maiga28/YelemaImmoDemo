from django.contrib import admin
from django.urls import path,include
from .views import index,team,about,contact,search
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from .views import custom_page_not_found

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('search/', search, name='search'),  
    path('team/', team, name='team'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('accounts/', include('allauth.urls')),
    path('profiles/', include('main_apps.profiles.urls')),
    path('gestion/', include('main_apps.gestion.urls')),
    path('client/', include('main_apps.client.urls')),
    path('location/', include('main_apps.gestion_location.urls')),
    path('locateur/', include('main_apps.locateur.urls')),   
    path('settings/', include('main_apps.settings.urls')),
    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Ajoutez un pattern générique pour gérer les URL non correspondantes
urlpatterns += [
    path('<path:unknown_path>', custom_page_not_found),
]