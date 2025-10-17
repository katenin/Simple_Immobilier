from django.db import models

class DocumentVerification(models.Model):
    TYPE_CHOICES = [
        ('ADU', 'Attestation de Droit d’Usage (ADU)'),
        ('ATTRIBUTION', 'Lettre d’attribution'),
        ('VILLAGEOISE', 'Attestation villageoise'),
    ]

    nom_demandeur = models.CharField(max_length=200)
    email = models.EmailField(default="non precisé")
    telephone = models.CharField(max_length=20)
    type_document = models.CharField(max_length=20, choices=TYPE_CHOICES)
    fichier = models.FileField(upload_to='documents_verification/')
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_demandeur} - {self.type_document}"
