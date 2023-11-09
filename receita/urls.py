''' Importa as minhas URLS '''
from django.urls import path
''' Importado todas URLS e VIEWS relacionadas '''
from . import views

''' Precisamos criar uma urlspattars 
    Primeiro parametro do Path é a = ROTA
    Segundo parametro do Path é a = RESPONSÁVEL 
    PELA VIEWS(views.nome que eu quero)
    Terceiro parametro do Path é a = NAME SPACE
'''
urlpatterns = [
    path('', views.index, name='index'),
    # Criando a rota de receita
    # path('nome que eu quero na url', metodo da views.py, nome para o metodo)
    # Prevendo o ID da RECEITA
    path('<int:receita_id>', views.receita, name='receita'), 
    # Criando o buscado da minha página
    path('buscar', views.buscar, name='buscar')
]



