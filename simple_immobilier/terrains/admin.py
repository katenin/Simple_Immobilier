from django.contrib import admin
from .models import Terrain

@admin.register(Terrain)
class TerrainAdmin(admin.ModelAdmin):
    list_display = ('titre', 'localisation', 'superficie', 'prix', 'disponible', 'date_ajout')
    search_fields = ('titre', 'localisation')
    list_filter = ('disponible', 'localisation')
