from django.db import models

# Criando uma Classe para interligar com meu banco de dados
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    # Criando uam CLASSE para referencia o nome da pessoa
    def __str__(self):
        return self.nome
