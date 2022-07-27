from django.forms import ModelForm
from .models import user as user
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext as _

class SignUpForm(ModelForm):

    class Meta:
        model = user
        fields = '__all__'

    def save(self, commit=True, *args, **kwargs):
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get('password'))
        m.username = self.cleaned_data.get('username').lower()

        if commit:
            m.save()
        return m