from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloDepartamento
from APLICACION_EMPRESA.serializers.common import SerializadorMunicipioResumenDepartamento

class SerializadorDetalleDepartamento(serializers.ModelSerializer):

    Municipios = SerializadorMunicipioResumenDepartamento(many=True, read_only=True)

    class Meta:

        model = ModeloDepartamento

        fields = (
            "Id",
            "Nombre",
            "Codigo",
            "Municipios",
            "Estado",
            "FechaCreacion",
            "FechaActualizacion"
        )