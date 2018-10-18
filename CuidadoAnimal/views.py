from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import FrutaForm
from .models import Fruta


def listaUsuarios(request):
    queryset = Fruta.objects.raw('SELECT * FROM CuidadoAnimal_fruta')
    queryset2 = Fruta.objects.all()
    context = {
        "lista": queryset
    }
    return render(request, "index.html", context)


def get_fruta(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FrutaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("hola1")
            # process the data in form.cleaned_data as required
            # ...
            nombre = request.POST.get('fruta', '')
            frut = Fruta(nombre=nombre)
            frut.save()
            # redirect to a new URL:
        return HttpResponseRedirect('/contact/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FrutaForm()
        print("hola2")

    return render(request, 'fruta.html', {'form': form})
