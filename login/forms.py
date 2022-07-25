from dataclasses import field, fields
from .models import logindetails
from django.forms import ModelForm


class logindetails(ModelForm):
    class Meta:
        model = logindetails
        fields = '__all__'

    