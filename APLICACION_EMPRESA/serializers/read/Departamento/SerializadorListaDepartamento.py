from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloDepartamento

class SerializadorListaDepartamento(serializers.ModelSerializer):

    class Meta:

        model = ModeloDepartamento

        fields = (
            "Id",
            "Nombre",
            "Codigo",
            "Estado"
        )