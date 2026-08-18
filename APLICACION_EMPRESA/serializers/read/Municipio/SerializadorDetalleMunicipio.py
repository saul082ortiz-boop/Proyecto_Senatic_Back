from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloMunicipio
from APLICACION_EMPRESA.serializers.common import SerializadorDepartamentoResumen

class SerializadorDetalleMunicipio(serializers.ModelSerializer):

    Departamento = SerializadorDepartamentoResumen()

    class Meta:

        model = ModeloMunicipio

        fields = (
            "Id",
            "Nombre",
            "Codigo",
            "Departamento",
            "Estado",
            "FechaCreacion",
            "FechaActualizacion"
        )