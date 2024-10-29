from django import forms


class AdoptionForm(forms.Form):
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)
    number_of_guinea_pigs = forms.IntegerField()
    living_arrangement = forms.ChoiceField(
        choices=[('flat', 'Flat'), ('house', 'House')]
    )