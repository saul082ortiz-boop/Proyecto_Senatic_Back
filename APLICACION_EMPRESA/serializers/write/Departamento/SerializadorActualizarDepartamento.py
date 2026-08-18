from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloDepartamento

class SerializadorActualizarDepartamento(serializers.ModelSerializer):

    class Meta:
        model = ModeloDepartamento

        fields = (
            "Nombre",
            "Codigo",
        )