from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloMunicipio

class SerializadorListaMunicipio(serializers.ModelSerializer):

    Departamento = serializers.CharField(source="Departamento.Nombre")

    class Meta:

        model = ModeloMunicipio

        fields = (
            "Id",
            "Nombre",
            "Codigo",
            "Departamento",
            "Estado"
        )