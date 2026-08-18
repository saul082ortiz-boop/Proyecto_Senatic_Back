from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloEmpresa

class SerializadorEmpresaResumenServicio(serializers.ModelSerializer):

    class Meta:
    
        model = ModeloEmpresa

        fields = (
            "Id",
            "Nit",
            "RazonSocial",
            "Logo"
        )