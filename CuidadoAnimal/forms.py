from django import forms


class FrutaForm(forms.Form):
    fruta = forms.CharField(label='ingrese fruta', max_length=100)
