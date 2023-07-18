"""
This module defines the application configuration for the elearn app.

The `ElearnConfig` class extends the `AppConfig` class provided by Django and defines
the configuration settings for the elearn app. It specifies the default auto field,
the name of the app, and any other customizations needed.

Note: Add more details and explanations as necessary.
"""
from django.apps import AppConfig

class ElearnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elearn'
