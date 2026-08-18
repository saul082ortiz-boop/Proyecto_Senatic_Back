from django.contrib import admin

from APLICACION_EMPRESA.models import ModeloServicio


@admin.register(ModeloServicio)
class ServicioAdmin(admin.ModelAdmin):

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