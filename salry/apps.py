from django.apps import AppConfig



class SalryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'salry'

    def ready(self):
        return super().ready()
