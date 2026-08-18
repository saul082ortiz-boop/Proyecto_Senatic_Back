from rest_framework import serializers


class SerializadorContrasenaOlvidada(serializers.Serializer):

    Correo = serializers.EmailField()