from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_password

class user(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=10, validators=[validate_password])
    phonenumber = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    
    def __str__(self):
        return self.username
        
