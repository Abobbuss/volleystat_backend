from django.contrib import admin
from django.apps import apps

# Регистрация всех моделей
app = apps.get_app_config('appstatistics')
for model_name, model in app.models.items():
    admin.site.register(model)
