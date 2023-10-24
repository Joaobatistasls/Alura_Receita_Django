from django.shortcuts import render

def index(request):
    # Criando minha variavel com os nomes da receita
    receita = {
        1: 'Lasanha',
        2: 'Torta', 
        3: 'Sopa de Legumes',
        4: 'Bolo'
    }
    # Criando a variavel dados para guarda as minha receitas
    dados = {
        'nome_das_receitas': receita
    }
    # Usando o dados para renderizar minha receitas na tela
    return render(request,'index.html', dados)

# criando uma função para o meu link receita.
def receita(request):
    return render(request, 'receita.html')