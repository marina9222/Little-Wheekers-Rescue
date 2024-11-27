from django import forms
from .models import Adoption


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        exclude = ['guinea_pig', 'adopter', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control form-control-lg',
            })
