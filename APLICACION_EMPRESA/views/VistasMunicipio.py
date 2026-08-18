from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from APLICACION_EMPRESA.models import ModeloMunicipio
from APLICACION_EMPRESA.serializers.read.Municipio import SerializadorDetalleMunicipio, SerializadorListaMunicipio
from APLICACION_EMPRESA.serializers.write.Municipio import SerializadorActualizarMunicipio, SerializadorCrearMunicipio
from APLICACION_EMPRESA.services import ServicioMunicipio
from APLICACION_USUARIOS.serializers.common import SerializadorVacio

class VistasMunicipio(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
    ):

    #permission_classes=[IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return SerializadorListaMunicipio
        if self.action == "retrieve":
            return SerializadorDetalleMunicipio
        if self.action == "create":
            return SerializadorCrearMunicipio
        if self.action == "update":
            return SerializadorActualizarMunicipio
        return SerializadorVacio

    # def get_permissions(self):
    #     if self.action in ["list", "retrieve", "create", "update", "destroy"]:
    #         permission_classes = [EsSuperAdministrador]
    #     elif self.action == "Activar":
    #         permission_classes = [EsSuperAdministrador]
    #     elif self.action == "Obtener":
    #         permission_classes = [IsAuthenticated, PermisosPersonalizados]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    queryset = ModeloMunicipio.objects.all()

    # ===========================================
    # LISTAR (GET /Municipio/)
    # ===========================================
    def list(self, request):
        Municipios = ServicioMunicipio.ObtenerMunicipios()
        Serializador = SerializadorListaMunicipio(Municipios, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # OBTENER (GET /Municipio/{id}/)
    # ===========================================
    def retrieve(self, request, pk=None):
        Municipio = ServicioMunicipio.ObtenerMunicipioPorId(pk)
        Serializador = SerializadorDetalleMunicipio(Municipio)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # CREAR (POST /Municipio/)
    # ===========================================
    def create(self, request):
        Serializador = SerializadorCrearMunicipio(data=request.data)
        Serializador.is_valid(raise_exception=True)
        Municipio = ServicioMunicipio.CrearMunicipio(Serializador.validated_data)
        SerializadorRespuesta = SerializadorDetalleMunicipio(Municipio)
        return Response(SerializadorRespuesta.data, status=status.HTTP_201_CREATED)

    # ===========================================
    # ACTUALIZAR COMPLETO (PUT /Municipio/{id}/)
    # ===========================================
    def update(self, request, pk=None):
        Municipio = ServicioMunicipio.ObtenerMunicipioPorId(pk)
        Serializador = SerializadorActualizarMunicipio(Municipio, data=request.data)
        Serializador.is_valid(raise_exception=True)
        Municipio = ServicioMunicipio.ActualizarMunicipio(Municipio,Serializador.validated_data)
        return Response(SerializadorDetalleMunicipio(Municipio).data, status=status.HTTP_200_OK)

    # ===========================================
    # ACTIVAR (PATCH /Municipio/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    #@action(detail=True, methods=["patch"], permission_classes = [EsSuperAdministrador])
    def Activar(self, request, pk=None):
        Municipio = ServicioMunicipio.ObtenerMunicipioPorId(pk)
        ServicioMunicipio.ActivarMunicipio(Municipio)
        return Response({"Mensaje": "Municipio"}, status=status.HTTP_200_OK)

    # ===========================================
    # ELIMINAR (DELETE /Municipio/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    def destroy(self, request, pk=None):
        Municipio = ServicioMunicipio.ObtenerMunicipioPorId(pk)
        ServicioMunicipio.EliminarMunicipio(Municipio)
        return Response({"Mensaje": "Municipio Eliminado"}, status=status.HTTP_200_OK)