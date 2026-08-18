from django.contrib import admin

from APLICACION_EMPRESA.models import ModeloMunicipio


@admin.register(ModeloMunicipio)
class MunicipioAdmin(admin.ModelAdmin):

    list_display = (
        "Id",
        "Nombre",
        "Codigo",
        "Departamento",
        "Estado"
    )

    search_fields = (
        "Nombre",
        "Codigo",
    )

    list_filter = (
        "Departamento",
        "Estado",
    )

    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": (
                        "Nombre",
                        "Codigo",
                        "Departamento",
                    ),
                },
            ),
        )