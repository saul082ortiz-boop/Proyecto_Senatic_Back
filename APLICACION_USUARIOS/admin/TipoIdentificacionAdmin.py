from django.contrib import admin

from APLICACION_USUARIOS.models import ModeloTipoIdentificacion


@admin.register(ModeloTipoIdentificacion)
class TipoIdentificacionAdmin(admin.ModelAdmin):

    list_display = (
        "Id",
        "Nombre",
        "Abreviatura",
        "Estado"
    )

    search_fields = (
        "Nombre",
        "Abreviatura"
    )

    list_filter = (
        "Estado",
    )