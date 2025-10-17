from django.db import models

class DemandeSuivie(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=100, default="Non renseigné")
    numero_dossier = models.CharField(max_length=100)
    message = models.TextField()
    date_demande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.numero_dossier}"
