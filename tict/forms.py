from .models import User
from django import form

class RegistrationForm(form.ModelForm):
    class Meta:
        fields = ['email','username',]
