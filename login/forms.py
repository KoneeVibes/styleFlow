# from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class logindetails(forms.ModelForm):
    username = forms.CharField(label=_('name'))
    password = 
    class Meta:
        model = User
        fields = ['username', 'password']
        error_messages = {
            'username': {
                'unique': _('Enter another username. This one is taken')
            }
        }
        

    