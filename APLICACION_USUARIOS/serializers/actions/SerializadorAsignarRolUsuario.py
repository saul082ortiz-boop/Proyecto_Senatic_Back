from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloRol


class SerializadorAsignarRolUsuario(serializers.Serializer):

    UsuarioId = serializers.IntegerField()
    Roles = serializers.PrimaryKeyRelatedField(queryset=ModeloRol.objects.filter(Estado=True), many=True)