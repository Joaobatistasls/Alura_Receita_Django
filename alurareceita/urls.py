from django.contrib import admin
''' Importando o includes '''
from django.urls import path, include

urlpatterns = [
    # Criando mais um path
    # include('argumentos que queremos incluir')
    # include('nomedonossoapp.urls')
    path('', include('receita.urls')),
    path('admin/', admin.site.urls),
]
