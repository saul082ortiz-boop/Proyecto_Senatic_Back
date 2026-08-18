from django.contrib import admin

from APLICACION_EMPRESA.models import ModeloMunicipio

class MunicipioInline(admin.TabularInline):

    model = ModeloMunicipio
    extra = 1