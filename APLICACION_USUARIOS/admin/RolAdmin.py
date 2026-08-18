from django.contrib import admin

from APLICACION_USUARIOS.models import ModeloRol


@admin.register(ModeloRol)
class RolAdmin(admin.ModelAdmin):

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