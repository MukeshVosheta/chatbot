from django.apps import AppConfig
import nltk


class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'

    def ready(self):
        nltk.download('punkt')

