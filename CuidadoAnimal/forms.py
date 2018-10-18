from django import forms


class FrutaForm(forms.Form):
    nombre = forms.CharField(required=False, max_length=100)
