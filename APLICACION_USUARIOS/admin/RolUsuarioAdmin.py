from django.contrib import admin

from APLICACION_USUARIOS.models import ModeloRolUsuario


@admin.register(ModeloRolUsuario)
class RolUsuarioAdmin(admin.ModelAdmin):

    list_display = (
        "Usuario",
        "Rol",
        "Estado"
    )

    autocomplete_fields = (
        "Usuario",
        "Rol"
    )