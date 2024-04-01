from django.apps import AppConfig


class GestionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_apps.gestion'

    def ready(self):
        # Importez ici pour éviter les importations circulaires
        from . import signals
 #       signals.register_signals()
