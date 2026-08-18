from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action

from APLICACION_USUARIOS.models import ModeloTipoIdentificacion
from APLICACION_USUARIOS.permissions import EsSuperAdministrador
from APLICACION_USUARIOS.serializers.common import SerializadorVacio
from APLICACION_USUARIOS.services.ServicioTipoIdentificacion import ServicioTipoIdentificacion
from APLICACION_USUARIOS.serializers.read.TipoIdentificacion import SerializadorListaTipoIdentificacion, SerializadorDetalleTipoIdentificacion
from APLICACION_USUARIOS.serializers.write.TipoIdentificacion import SerializadorCrearTipoIdentificacion, SerializadorActualizarTipoIdentificacion

class VistasTipoIdentificacion(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
    ):

    permission_classes = [EsSuperAdministrador]

    def get_serializer_class(self):
        if self.action == "list":
            return SerializadorListaTipoIdentificacion
        if self.action == "retrieve":
            return SerializadorDetalleTipoIdentificacion
        if self.action == "create":
            return SerializadorCrearTipoIdentificacion
        if self.action == "update":
            return SerializadorActualizarTipoIdentificacion    
        return SerializadorVacio

    queryset = ModeloTipoIdentificacion.objects.all()

    #===========================================
    #LISTAR (GET /TipoIdentidicacion/)
    #===========================================
    def list(self, request):
        TipoIdentificaciones = ServicioTipoIdentificacion.ObtenerTiposIdentificaciones()
        Serializador = SerializadorListaTipoIdentificacion(TipoIdentificaciones, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    #===========================================
    #OBTENER (GET /TipoIdentidicacion/{id}/)
    #===========================================
    def retrieve(self, request, pk=None):
        TipoIdentificacion = ServicioTipoIdentificacion.ObtenerTipoIdentificacionPorId(pk)
        Serializador = SerializadorDetalleTipoIdentificacion(TipoIdentificacion)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    #===========================================
    #CREAR (POST /TipoIdentidicacion/)
    #===========================================
    def create(self, request):
        Serializador = SerializadorCrearTipoIdentificacion(data=request.data)
        Serializador.is_valid(raise_exception=True)
        TipoIdentificacion = ServicioTipoIdentificacion.CrearTipoIdentificacion(Serializador.validated_data)
        SerializadorRespuesta = SerializadorDetalleTipoIdentificacion(TipoIdentificacion)
        return Response(SerializadorRespuesta.data, status=status.HTTP_201_CREATED)

    #===========================================
    #ACTUALIZAR COMPLETO (PUT /TipoIdentidicacion/{id}/)
    #===========================================
    def update(self, request, pk=None):
        TipoIdentificacion = ServicioTipoIdentificacion.ObtenerTipoIdentificacionPorId(pk)
        Serializador = SerializadorActualizarTipoIdentificacion(TipoIdentificacion, data=request.data)
        Serializador.is_valid(raise_exception=True)
        TipoIdentificacion = ServicioTipoIdentificacion.ActualizarTipoIdentificacion(TipoIdentificacion,Serializador.validated_data)
        return Response(SerializadorDetalleTipoIdentificacion(TipoIdentificacion).data, status=status.HTTP_200_OK)

    #===========================================
    #ACTIVAR (PATCH /TipoIdentidicacion/{id}/)
    #===========================================
    @extend_schema(request=None, responses={200: None})
    @action(detail=True, methods=["patch"])
    def Activar(self, request, pk=None):
        TipoIdentificacion = ServicioTipoIdentificacion.ObtenerTipoIdentificacionPorId(pk)
        ServicioTipoIdentificacion.ActivarTipoIdentificacion(TipoIdentificacion)
        return Response({"Mensaje": "Tipo Identidicacion Activado"}, status=status.HTTP_200_OK)

    #===========================================
    #ELIMINAR (DELETE /TipoIdentidicacion/{id}/)
    #===========================================
    @extend_schema(request=None, responses={200: None})
    def destroy(self, request, pk=None):
        TipoIdentificacion = ServicioTipoIdentificacion.ObtenerTipoIdentificacionPorId(pk)
        ServicioTipoIdentificacion.EliminarTipoIdentificacion(TipoIdentificacion)
        return Response({"Mensaje": "Tipo Identidicacion Eliminado"}, status=status.HTTP_200_OK)