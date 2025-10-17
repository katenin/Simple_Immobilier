from django import forms
from .models import DocumentVerification

class DocumentVerificationForm(forms.ModelForm):
    class Meta:
        model = DocumentVerification
        fields = ['nom_demandeur', 'email', 'telephone', 'type_document', 'fichier']
        labels = {
            'nom_demandeur': 'Nom complet',
            'email': 'Adresse e-mail',
            'telephone': 'Numéro de téléphone',
            'type_document': 'Type de document',
            'fichier': 'Joindre le document',
        }
        widgets = {
            'nom_demandeur': forms.TextInput(attrs={
                'placeholder': 'Entrez votre nom complet',
                'class': 'form-control',
                'required': 'required',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Entrez votre adresse e-mail',
                'class': 'form-control',
                'required': 'required',
            }),
            'telephone': forms.TextInput(attrs={
                'placeholder': 'Entrez votre numéro de téléphone',
                'class': 'form-control',
                'required': 'required',
            }),
            'type_document': forms.Select(attrs={
                'class': 'form-select',
                'required': 'required',
            }),
            'fichier': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,image/*',  # Limite aux PDF et images
                'required': 'required',
            }),
        }

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        if not telephone:
            raise forms.ValidationError("Le numéro de téléphone est obligatoire.")
        # Optionnel : vérifie format ivoirien simple (07xx/01xx/05xx)
        import re
        if not re.match(r'^(07|05|01)\d{6,8}$', telephone):
            raise forms.ValidationError("Numéro de téléphone invalide (ex: 07000000).")
        return telephone
