from django.db import models
from datetime import datetime

class Receita(models.Model):
    # Criando os campos da minha receita.
    # Criando o nome da receita - CharField - Para texto
    nome_receita = models.CharField(max_length=200)
    # Ingredientes - TextField - Para texto maior  
    ingredientes = models.TextField()
    # Modo de Preparo - TextField - Para texto maior 
    modo_preparo = models.TextField()
    # Tempo de Preparo - IntegerField - Para numero inteiro
    tempo_preparo = models.IntegerField()
    # Rendimento - CharField - Para texto
    redimento = models.CharField(max_length=100)
    # Categoria - CharField - Para texto
    categoria = models.CharField(max_length=100)
    # Data da Receita - Datetime - Para Data e Hora
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    