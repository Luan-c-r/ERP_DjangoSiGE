# -*- coding: utf-8 -*-

from django.urls import path, re_path, include
from django.contrib import admin
from django.conf.urls.static import static
from .configs.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),  # Substituído por path
    path('', include('djangosige.apps.base.urls')),  # Substituído por path
    path('login/', include('djangosige.apps.login.urls')),  # Substituído por path
    path('cadastro/', include('djangosige.apps.cadastro.urls')),  # Substituído por path
    path('fiscal/', include('djangosige.apps.fiscal.urls')),  # Substituído por path
    path('vendas/', include('djangosige.apps.vendas.urls')),  # Substituído por path
    path('compras/', include('djangosige.apps.compras.urls')),  # Substituído por path
    path('financeiro/', include('djangosige.apps.financeiro.urls')),  # Substituído por path
    path('estoque/', include('djangosige.apps.estoque.urls')),  # Substituído por path
    path('saas/', include('djangosige.apps.saas.urls')), # Criado com path
]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
