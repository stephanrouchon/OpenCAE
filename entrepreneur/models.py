from django.db import models
from authentication.models import User
from .validators import (validate_french_ss_number,
                         validate_iban)
from datetime import date

SEXE_CHOICES = [
    ("H", "Homme"),
    ("F", "Femme"),
]

FAMILY_SITUATION_CHOICES = [
    ("CE", "Célibataire"),
    ("MA", "Marié(e)"),
    ("CO", "Concubin(e)"),
    ("VE", "Veuf ou Veuve"),
    ("PA", "Pacsé"),

]


class Nationality(models.Model):
    code = models.CharField(max_length=10, unique=True)
    libelle = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Nationalité"
        verbose_name_plural = "Nationalités"

    def __str__(self):
        return self.libelle


class Study_Level(models.Model):
    level = models.PositiveIntegerField()
    description = models.CharField(max_length=100)


class Entrepreneur(models.Model):
    entrepreneur = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_place = models.CharField(max_length=25,
                                   verbose_name="Lieu de naissance")
    nationality = models.ForeignKey(Nationality, null=True, blank=True,
                                    on_delete=models.SET_NULL)
    address = models.CharField(max_length=100,
                               verbose_name="adresse")
    city_code = models.PositiveIntegerField(verbose_name="Code postal")
    city = models.CharField(max_length=100, verbose_name="Ville")
    created_at = models.DateTimeField(auto_created=True,
                                      verbose_name="date de création")
    email = models.EmailField()
    phone = models.CharField(max_length=8,
                             verbose_name="Telephone fixe")
    mobile = models.CharField(max_length=8,
                              verbose_name="Portable")
    sexe = models.CharField(max_length=1,
                            choices=SEXE_CHOICES,
                            verbose_name="sexe")
    validity_date = models.DateField(
        verbose_name="date de validité du titre de séjour"
        )
    ss_number = models.CharField(
        max_length=15,
        verbose_name="numéro de sécurité sociale",
        blank=True,
        null=True,
        validators=[validate_french_ss_number]
    )
    family_situation = models.CharField(max_length=2,
                                        choices=FAMILY_SITUATION_CHOICES,
                                        verbose_name="Situation familliale"
                                        )
    children_number = models.IntegerField(verbose_name="Nombre d'enfants")
    study_level = models.ForeignKey(Study_Level, null=True,
                                    on_delete=models.SET_NULL,
                                    verbose_name="Niveau d'étude")

    def age(self):
        if not self.birthdate:
            return None
        today = date.today()
        age = today.year - self.birthdate.year - (
            (today.month, today.day) < (self.birthdate.month,
                                        self.birthdate.day)
        )
        return age


class BankAccount(models.Model):
    titulaire = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    iban = models.CharField(max_length=34, verbose_name="IBAN",
                            validators=[validate_iban])
    bic = models.CharField(max_length=20, verbose_name="BIC")
    agency = models.CharField(max_length=100, verbose_name="Domiciliation")
    purpose = models.CharField(max_length=20, verbose_name="Utilisation")

    class Meta:
        verbose_name = "Compte bancaire"
        verbose_name_plural = "Comptes bancaires"
