from django import forms
from .models import Adoption


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        exclude = ['guinea_pig', 'adopter', 'created_at']