from django.contrib import admin

from APLICACION_EMPRESA.models import ModeloTipoEmpresa


@admin.register(ModeloTipoEmpresa)
class TipoEmpresaAdmin(admin.ModelAdmin):

    list_display = (
        "Id",
        "Nombre",
        "Estado"
    )

    search_fields = (
        "Nombre",
    )

    list_filter = (
        "Estado",
    )