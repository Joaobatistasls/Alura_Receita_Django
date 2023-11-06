from django.contrib import admin
''' Importando o includes '''
from django.urls import path, include
# Importando o settings
from django.conf import settings
# Importando os meus arquivos estaticos
from django.conf.urls.static import static

urlpatterns = [
    # Criando mais um path
    # include('argumentos que queremos incluir')
    # include('nomedonossoapp.urls')
    path('', include('receita.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
