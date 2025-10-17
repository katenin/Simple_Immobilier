from django.db import models

class Terrain(models.Model):
    titre = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    superficie = models.DecimalField(max_digits=10, decimal_places=2)
    prix = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='terrains/')
    disponible = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} - {self.localisation}"
