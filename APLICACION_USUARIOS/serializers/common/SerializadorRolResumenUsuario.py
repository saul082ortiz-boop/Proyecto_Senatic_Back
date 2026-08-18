from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloRol

class SerializadorRolResumenUsuario(serializers.ModelSerializer):

    class Meta:
    
        model = ModeloRol

        fields = (
            "Id",
            "Nombre"
        )