from django import forms
from .models import People


class PepoleForm(forms.ModelForm):
    class  Meta:
        model=People
        fields='__all__'