from django.contrib import admin

from APLICACION_EMPRESA.admin.inlines import ServicioEmpresaInline
from APLICACION_EMPRESA.models import ModeloEmpresa


@admin.register(ModeloEmpresa)
class EmpresaAdmin(admin.ModelAdmin):

    list_display = (
        "Id",
        "TipoEmpresa",
        "RazonSocial",
        "Nit",
        "Municipio",
        "Telefono",
        "Correo",
        "Estado",
    )

    search_fields = (
        "RazonSocial",
        "Nit",
        "Correo",
    )

    list_filter = (
        "TipoEmpresa",
        "Municipio__Departamento",
        "Estado",
    )

    inlines = [
        ServicioEmpresaInline
    ]