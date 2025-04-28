from django import forms
from adoptions.models import GuineaPig


class GuineaPigForm(forms.ModelForm):
    class Meta:
        model = GuineaPig
        fields = ['name', 'birth_year', 'image', 'gender', 'adopted']