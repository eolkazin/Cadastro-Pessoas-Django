from django.shortcuts import render
from .models import Pessoas
# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        idade = request.POST.get('idade')
        p = Pessoas(nome=nome, sobrenome=sobrenome, idade=idade)
        p.save()
        print(p)
    return render(request, 'cadastro.html')