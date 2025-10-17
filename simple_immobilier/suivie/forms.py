from django import forms
from .models import DemandeSuivie

class DemandeSuivieForm(forms.ModelForm):
    class Meta:
        model = DemandeSuivie
        fields = ['nom', 'email', 'telephone', 'numero_dossier', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre adresse e-mail'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre contact'}),
            'numero_dossier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: ACD-00*-202*********'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Expliquez votre demande'}),
        }
