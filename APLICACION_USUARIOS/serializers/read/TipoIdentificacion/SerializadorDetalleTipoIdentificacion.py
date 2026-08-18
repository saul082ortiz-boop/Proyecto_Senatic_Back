from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloTipoIdentificacion


class SerializadorDetalleTipoIdentificacion(serializers.ModelSerializer):

    class Meta:

        model = ModeloTipoIdentificacion

        fields = (
            "Id",
            "Nombre",
            "Abreviatura",
            "Estado",
            "FechaCreacion",
            "FechaActualizacion"
        )