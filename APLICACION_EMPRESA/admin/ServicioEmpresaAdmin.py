from django.contrib import admin

from APLICACION_EMPRESA.models import ModeloServicioEmpresa


@admin.register(ModeloServicioEmpresa)
class ServicioEmpresaAdmin(admin.ModelAdmin):

    list_display = (
        "Empresa",
        "Servicio",
        "Estado"
    )

    autocomplete_fields = (
        "Empresa",
        "Servicio"
    )