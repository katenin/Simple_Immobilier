from django.contrib import admin
from .models import DemandeSuivie

@admin.register(DemandeSuivie)
class DemandeSuivieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'numero_dossier', 'date_demande')
    search_fields = ('nom', 'numero_dossier')
    list_filter = ('date_demande',)
