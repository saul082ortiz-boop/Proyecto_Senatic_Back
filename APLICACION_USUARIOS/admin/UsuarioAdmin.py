from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from APLICACION_USUARIOS.admin.inlines import RolUsuarioInline
from APLICACION_USUARIOS.models import ModeloUsuario


@admin.register(ModeloUsuario)
class UsuarioAdmin(UserAdmin):

    ordering = ("Correo",)

    list_display = (
        "Id",
        "Correo",
        "Nombre",
        "Apellido",
        "Telefono",
        "is_staff",
        "is_superuser",
        "Estado"
    )

    search_fields = (
        "Correo",
        "Nombre",
        "Apellido",
        "NumeroIdentificacion"
    )

    list_filter = (
        "is_staff",
        "is_superuser",
        "Estado",
        "groups",
    )

    fieldsets = (

        ("Información Personal", {
            "fields": (
                "Correo",
                "password",
                "Nombre",
                "Apellido",
                "Telefono",
                "NumeroIdentificacion",
                "TipoIdentificacion"
            )
        }),

        ("Permisos", {
            "fields": (
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
                "Estado"
            )
        }),

        ("Fechas", {
            "fields": (
                "last_login",
                "FechaCreacion",
                "FechaActualizacion"
            )
        })
    )

    readonly_fields = (
        "last_login",
        "FechaCreacion",
        "FechaActualizacion"
    )

    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": (
                        "Correo",
                        "Nombre",
                        "Apellido",
                        "Telefono",
                        "NumeroIdentificacion",
                        "TipoIdentificacion",
                        "password1",
                        "password2",
                        "is_staff",
                        "is_superuser",
                    ),
                },
            ),
        )

    inlines = [
        RolUsuarioInline
    ]
