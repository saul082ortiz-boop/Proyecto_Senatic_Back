from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloMunicipio

class SerializadorActualizarMunicipio(serializers.ModelSerializer):

    class Meta:
        model = ModeloMunicipio

        fields = (
            "Nombre",
            "Codigo",
            "Departamento"
        )