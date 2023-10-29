from django.contrib import admin
# Importando o models Pessoa criado
from .models import Pessoa

class ListandoPessoa(admin.ModelAdmin):
    # Usando o list_display para coloca o nome o id da receita 
    # no Django Admin
    list_display = ('id', 'nome', 'email')
    # Deixando outros componentes como link no Admin
    list_display_links = ('id', 'nome')
    # Adicionando um campo de buscar no Django Admin
    # search_fields = ('nome do campo que queremos pesquisar')
    search_fields = ('nome',)
    # Adicionando uma Paginação para que o scroll não fique grande
    # list_per_page = numero de conteudo que quero por pagina
    list_per_page = 2

# Registrando o modelo de pessoas criado
admin.site.register(Pessoa, ListandoPessoa)
