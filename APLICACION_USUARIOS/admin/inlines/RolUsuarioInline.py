from django.contrib import admin

from APLICACION_USUARIOS.models import ModeloRolUsuario

class RolUsuarioInline(admin.TabularInline):

    model = ModeloRolUsuario
    extra = 1
    autocomplete_fields = (
        "Rol",
    )