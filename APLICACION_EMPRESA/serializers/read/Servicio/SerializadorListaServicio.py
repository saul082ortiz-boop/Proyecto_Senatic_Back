from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloServicio

class SerializadorListaServicio(serializers.ModelSerializer):

    class Meta:

        model = ModeloServicio

        fields = (
            "Id",
            "Nombre",
            "Estado"
        )