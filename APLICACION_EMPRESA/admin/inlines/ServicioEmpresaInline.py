from django.contrib import admin

from APLICACION_EMPRESA.models import ModeloServicioEmpresa

class ServicioEmpresaInline(admin.TabularInline):

    model = ModeloServicioEmpresa
    extra = 1