from django.shortcuts import render

def index(request):
    # Usando o método render() para rederizar minha página
    # render(request, 'nome do arquivo pra renderizar.formato arq')
    return render(request,'index.html')

# criando uma função para o meu link receita.
def receita(request):
    return render(request, 'receita.html')