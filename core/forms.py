from .models import User
from django import forms


class newUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
