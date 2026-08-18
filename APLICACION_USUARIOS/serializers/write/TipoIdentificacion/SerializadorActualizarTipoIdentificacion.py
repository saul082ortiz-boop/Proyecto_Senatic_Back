from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloTipoIdentificacion

class SerializadorActualizarTipoIdentificacion(serializers.ModelSerializer):

    class Meta:
        model = ModeloTipoIdentificacion
        
        fields = (
            "Nombre",
            "Abreviatura",
        )