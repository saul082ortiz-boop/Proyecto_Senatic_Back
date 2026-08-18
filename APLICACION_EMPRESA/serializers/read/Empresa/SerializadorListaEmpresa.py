from rest_framework import serializers

from APLICACION_EMPRESA.models import ModeloEmpresa
from APLICACION_EMPRESA.serializers.common import SerializadorMunicipioResumen, SerializadorTipoEmpresaResumen
from APLICACION_USUARIOS.serializers.common import SerializadorUsuarioResumenRol

class SerializadorListaEmpresa(serializers.ModelSerializer):

    Municipio = SerializadorMunicipioResumen()
    TipoEmpresa = SerializadorTipoEmpresaResumen()
    Administrador = SerializadorUsuarioResumenRol()

    class Meta:

        model = ModeloEmpresa

        fields = (
            "Id",
            "Nit",
            "RazonSocial",
            "Logo",
            "Municipio",
            "Telefono",
            "Correo",
            "TipoEmpresa",
            "Administrador",
            "Estado",
        )










