from django import forms


class FrutaForm(forms.Form):
    nombre = forms.CharField(required=False, max_length=100)


# Formulario de registro de un dueño de mascota
class RegisterClientForm(forms.Form):
    nombre = forms.CharField(label='nombre: ', max_length=100)
    apellido = forms.CharField(label='apellido: ', max_length=100)
    cedula = forms.IntegerField(label='nombre: ')
    password = forms.CharField(label='password: ', max_length=100)
    direccion = forms.CharField(label='direccion: ', max_length=100)
    telefono = forms.IntegerField(label='telefono: ')
    correo = forms.CharField(label='correo: ', max_length=100)
    imagen = forms.ImageField();


class RegisterDuenoVetForm(forms.Form):
    Nombres = forms.CharField(label='nombres: ', max_length=100)
    Apellidos = forms.CharField(label='Apellidos: ', max_length=100)
    NombreUsuario = forms.CharField(label='NombreUsuario: ', max_length=100)
    Email = forms.CharField(label='Email: ', max_length=100)
    Password = forms.CharField(label='Password: ', max_length=100)
    ConfPassword = forms.CharField(label='ConfPass: ', max_length=100)


class RegisterClinicaForm(forms.Form):
    Nombre = forms.CharField(label='Nombre: ', max_length=100)
    Logotipo = forms.ImageField();
    Telefono = forms.IntegerField;
    Ciudad = forms.CharField(label='Ciudad: ', max_length=100)
    Localidad = forms.CharField(label='Localidad: ', max_length=100)
    Barrio = forms.CharField(label='Barrio: ', max_length=100)
    Direccion = forms.CharField(label='Direccion: ', max_length=100)
    HoraA = forms.TimeField(label='HoraA: ')
    HoraC = forms.TimeField(label='HoraC: ')


class LogInForm(forms.Form):
    NombreUsuario = forms.CharField(label='NombreUsuario: ', max_length=100)
    Password = forms.CharField(label='Password: ', max_length=1000)
