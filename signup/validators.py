from django.core.exceptions import ValidationError

def validate_phonenumber(value):
    if len(value) < 10:
        raise ValidationError('Not a correct phome number')