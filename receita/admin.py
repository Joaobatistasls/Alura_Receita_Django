from django.contrib import admin
# Importando nossa Class Receita de 'models.py'
from .models import Receita

# Criando uma Class para mudar as informações no Admin
class ListandoReceitas(admin.ModelAdmin):
    # Usando o list_display para coloca o nome o id da receita 
    # no Django Admin
    list_display = ('id', 'nome_receita', 'categoria', 'publicada')
    # Deixando outros componentes como link no Admin
    list_display_links = ('id', 'nome_receita')
    # Adicionando um campo de buscar no Django Admin
    # search_fields = ('nome do campo que queremos pesquisar')
    search_fields = ('nome_receita',)
    # Adicionando um filtro de categoria no Django Admin 
    # list_filter = ('nome do campo do que eu quero que seja o filtro',)
    list_filter = ('categoria',)
    # Adicionando uma Paginação para que o scroll não fique grande
    # list_per_page = numero de conteudo que quero por pagina
    list_per_page = 5
    # Para dizer que o campo do Admin é Editavel
    list_editable = ('publicada',)

# Rigistrando meu modelo de receita e Lista da Receita
admin.site.register(Receita, ListandoReceitas)

