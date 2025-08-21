import re
from django.core.exceptions import ValidationError


def validate_french_ss_number(value):
    """
    Valide un numéro de sécurité sociale français (NIR) :
    - 13 chiffres + 2 chiffres de clé (optionnel)
    - Vérifie la clé de contrôle si présente
    """
    if not value:
        return
    value = value.replace(' ', '')
    if not re.fullmatch(r'\d{13,15}', value):
        raise ValidationError(
            "Le numéro de sécurité sociale doit contenir 13 à 15 chiffres.")
    nir = value[:13]
    if len(value) >= 15:
        key = int(value[13:15])
        try:
            nir_int = int(nir)
        except ValueError:
            raise ValidationError(
                "Le numéro de sécurité sociale doit être numérique.")
        expected_key = 97 - (nir_int % 97)
        if key != expected_key:
            raise ValidationError(
                f"Clé de contrôle incorrecte : attendu {expected_key:02d}.")


def validate_iban(value):
    """
    Valide un IBAN selon la norme internationale
    (structure et clé de contrôle).
    """
    if not value:
        return
    iban = value.replace(' ', '').upper()
    # Vérifie la longueur minimale et maximale
    if not 15 <= len(iban) <= 34:
        raise ValidationError(
            "L'IBAN doit contenir entre 15 et 34 caractères.")
    # Vérifie le format général (lettres et chiffres)
    if not re.match(r'^[A-Z0-9]+$', iban):
        raise ValidationError(
            "L'IBAN ne doit contenir que des lettres et des chiffres.")
    # Vérification de la clé de contrôle
    iban_rearranged = iban[4:] + iban[:4]
    iban_numeric = ''
    for c in iban_rearranged:
        if c.isdigit():
            iban_numeric += c
        else:
            iban_numeric += str(ord(c) - 55)
    if int(iban_numeric) % 97 != 1:
        raise ValidationError(
            "L'IBAN est invalide (clé de contrôle incorrecte).")
