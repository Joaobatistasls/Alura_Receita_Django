from django.db import models
from datetime import datetime
# Importando minha classe de PESSOAS DO 2 APP(pessoas)
from pessoas.models import Pessoa

class Receita(models.Model):
    # Criando o RELACIONAMENTO entre os APPS
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
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
    redimento = models.CharField(max_length=101)
    # Categoria - CharField - Para texto
    categoria = models.CharField(max_length=100)
    # Data da Receita - Datetime - Para Data e Hora
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    # Criando um FILTRO para nossas RECEITA ESTÁ PUBLICADA
    # Primeiro argumento do BooleanField(), é um valor DEFAULT = True ou False
    publicada = models.BooleanField(default=False)
    # Criando campo para colocar Imagem 
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)