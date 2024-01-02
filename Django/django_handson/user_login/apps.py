from django.apps import AppConfig


class UserLoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_login'

    def ready(self):
        import user_login.signals