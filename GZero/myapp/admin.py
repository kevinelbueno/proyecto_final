# myapp/admin.py

from django.contrib import admin
from .models import Art, Artista  # Corrige 'Arte' a 'Art'

admin.site.register(Art)
admin.site.register(Artista)
