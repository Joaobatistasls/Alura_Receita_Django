from django.shortcuts import render
# Importando minha Class Receita para a views.py
from .models import Receita

def index(request):
    # Pegando todos os objetos da minha Rceita e do Admin
    receitas = Receita.objects.all()

    # Criando a variavel dados para guarda as minha receitas
    dados = {
        'receitas': receitas
    }
    # Usando o dados para renderizar minha receitas na tela
    return render(request,'index.html', dados)

# criando uma função para o meu link receita.
def receita(request):
    return render(request, 'receita.html')