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
    path('receita', views.receita, name='receita')
]

