from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloEmpresa

class SerializadorActualizarEmpresa(serializers.ModelSerializer):

    class Meta:
        model = ModeloEmpresa

        fields = (
            "Nit",
            "RazonSocial",
            "Direccion",
            "Municipio",
            "Barrio",
            "Telefono",
            "Correo",
            "CuposHora",
            "TipoEmpresa",
            "Administrador",
        )