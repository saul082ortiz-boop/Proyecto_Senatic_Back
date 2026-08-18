from rest_framework import serializers


class SerializadorIniciarSesion(serializers.Serializer):

    Correo = serializers.EmailField()
    password = serializers.CharField(write_only=True)