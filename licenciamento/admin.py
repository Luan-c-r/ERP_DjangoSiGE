from django.contrib import admin
from .models import TipoNegocioCliente, ClienteLicenciado, PlanoLicenca, Licenca, WidgetDashboard, LayoutDashboard

admin.site.register(TipoNegocioCliente)
admin.site.register(ClienteLicenciado)
admin.site.register(PlanoLicenca)
admin.site.register(Licenca)
admin.site.register(WidgetDashboard)
admin.site.register(LayoutDashboard)

