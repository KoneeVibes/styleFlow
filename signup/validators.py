from django.core.exceptions import ValidationError

def validate_password(value):
    special_characters = '!'
    if special_characters in value:
        raise ValidationError('password should noot contain !')