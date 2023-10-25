from django.contrib import admin
# Importando nossa Class Receita de 'models.py'
from .models import Receita

# Rigistrando meu modelo de receita
admin.site.register(Receita)

