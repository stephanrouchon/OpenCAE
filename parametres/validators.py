from django.forms import ValidationError


def validate_account(value):
    if value and len(value) != 8:
        raise ValidationError("Le compte auxiliaire doit faire exactement 8 \
                              caractères ou être vide.")
