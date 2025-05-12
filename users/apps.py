from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
        # The import statement is used to ensure that the signals are registered
        # when the app is ready. This is necessary because signals are not automatically
        # imported when the app is loaded, so we need to explicitly import them here.
