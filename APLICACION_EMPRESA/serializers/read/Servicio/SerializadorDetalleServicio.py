from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloServicio
from APLICACION_EMPRESA.serializers.common import SerializadorEmpresaResumenServicio

class SerializadorDetalleServicio(serializers.ModelSerializer):

    Empresas = SerializadorEmpresaResumenServicio(many=True, read_only=True)

    class Meta:

        model = ModeloServicio

        fields = (
            "Id",
            "Nombre",
            "Empresas",
            "Estado",
            "FechaCreacion",
            "FechaActualizacion"
        )