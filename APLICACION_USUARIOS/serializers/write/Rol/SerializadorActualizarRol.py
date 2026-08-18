from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloRol

class SerializadorActualizarRol(serializers.ModelSerializer):

    class Meta:
        model = ModeloRol

        fields = (
            "Nombre",
        )