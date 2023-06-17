from django.apps import AppConfig
import environ

class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(env_file='./.env')