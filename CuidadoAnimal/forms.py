from django import forms


class FrutaForm(forms.Form):
    nombre = forms.CharField(required=False, max_length=100)


class LogInForm(forms.Form):
    nombre = forms.CharField(label='nombre: ', max_length=100)
    apellido = forms.CharField(label='apellido: ', max_length=100)
    cedula = forms.IntegerField(label='nombre: ')
    password = forms.CharField(label='password: ', max_length=100)
    direccion = forms.CharField(label='direccion: ', max_length=100)
    telefono = forms.IntegerField(label='telefono: ')
    correo = forms.CharField(label='correo: ', max_length=100)
