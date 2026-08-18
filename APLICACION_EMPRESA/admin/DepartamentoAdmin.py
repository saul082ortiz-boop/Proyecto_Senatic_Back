from django.contrib import admin

from APLICACION_EMPRESA.admin.inlines import MunicipioInline
from APLICACION_EMPRESA.models import ModeloDepartamento


@admin.register(ModeloDepartamento)
class DepartamentoAdmin(admin.ModelAdmin):

    list_display = (
        "Id",
        "Nombre",
        "Codigo",
        "Estado"
    )

    search_fields = (
        "Nombre",
        "Codigo",
    )

    list_filter = (
        "Estado",
    )

    inlines = [
        MunicipioInline
    ]