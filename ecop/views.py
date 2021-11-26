from django.shortcuts import render

from .models import Enderecos


def index(request):
    return render(request, 'index.html')


def locais(request):
    enderecos = Enderecos.objects.all()

    context = {
        'enderecos': enderecos
    }
    return render(request, 'locais.html', context)


def localizacao(request):
    return render(request, 'localizacao.html')


def saibamais(request):
    return render(request, 'saibamais.html')


from django.shortcuts import render

# Create your views here.
