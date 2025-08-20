from django.shortcuts import render
from cadastro.models import Pessoas

# Create your views here.
def lista(request):
    pessoas = Pessoas.objects.all()  # pega tudo do banco
    return render(request, 'lista.html', {'pessoas': pessoas})
