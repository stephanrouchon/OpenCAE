from django.db import models


class Nationality(models.Model):
    code = models.CharField(max_length=10, unique=True)
    libelle = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Nationalité"
        verbose_name_plural = "Nationalités"

    def __str__(self):
        return self.libelle


class Status(models.Model):
    code = models.CharField(max_length=10, unique=True)
    libellé = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Statut"
        verbose_name_plural = "Statuts"
