# Importando o get_list e get_object
from django.shortcuts import render, get_list_or_404, get_object_or_404
# Importando minha Class Receita para a views.py
from .models import Receita

def index(request):
    # Criando um FILTRO para pegar apenas as receitas 
    # Publicada na Página e no Admin
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    # Criando a variavel dados para guarda as minha receitas
    dados = {
        'receitas': receitas
    }
    # Usando o dados para renderizar minha receitas na tela
    return render(request,'index.html', dados)

# criando uma função para o meu link receita.
# Inserindo o ID na RECEITA
def receita(request, receita_id):
    # Guardando a informações da URL com o metedo get_object_or_404
    receita = get_object_or_404(Receita, pk=receita_id)

    # Passando a informação para a nossa página
    receita_a_exibir = {
        'receita': receita
    }

    return render(request, 'receita.html', receita_a_exibir)


# Criando o metodo de Pesquisa da minha receita.
def buscar(request):
    return render(request, 'buscar.html')