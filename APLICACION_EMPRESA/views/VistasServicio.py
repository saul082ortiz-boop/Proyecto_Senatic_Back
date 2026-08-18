from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from APLICACION_EMPRESA.models import ModeloServicio
from APLICACION_EMPRESA.serializers.read.Servicio import SerializadorDetalleServicio, SerializadorListaServicio
from APLICACION_EMPRESA.serializers.write.Servicio import SerializadorActualizarServicio, SerializadorCrearServicio
from APLICACION_EMPRESA.services import ServicioServicio
from APLICACION_USUARIOS.serializers.common import SerializadorVacio

class VistasServicio(
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
            return SerializadorListaServicio
        if self.action == "retrieve":
            return SerializadorDetalleServicio
        if self.action == "create":
            return SerializadorCrearServicio
        if self.action == "update":
            return SerializadorActualizarServicio
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

    queryset = ModeloServicio.objects.all()

    # ===========================================
    # LISTAR (GET /Servicio/)
    # ===========================================
    def list(self, request):
        Servicios = ServicioServicio.ObtenerServicios()
        Serializador = SerializadorListaServicio(Servicios, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # OBTENER (GET /Servicio/{id}/)
    # ===========================================
    def retrieve(self, request, pk=None):
        Servicio = ServicioServicio.ObtenerServicioPorId(pk)
        Serializador = SerializadorDetalleServicio(Servicio)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # CREAR (POST /Servicio/)
    # ===========================================
    def create(self, request):
        Serializador = SerializadorCrearServicio(data=request.data)
        Serializador.is_valid(raise_exception=True)
        Servicio = ServicioServicio.CrearServicio(Serializador.validated_data)
        SerializadorRespuesta = SerializadorDetalleServicio(Servicio)
        return Response(SerializadorRespuesta.data, status=status.HTTP_201_CREATED)

    # ===========================================
    # ACTUALIZAR COMPLETO (PUT /Servicio/{id}/)
    # ===========================================
    def update(self, request, pk=None):
        Servicio = ServicioServicio.ObtenerServicioPorId(pk)
        Serializador = SerializadorActualizarServicio(Servicio, data=request.data)
        Serializador.is_valid(raise_exception=True)
        Servicio = ServicioServicio.ActualizarServicio(Servicio,Serializador.validated_data)
        return Response(SerializadorDetalleServicio(Servicio).data, status=status.HTTP_200_OK)

    # ===========================================
    # ACTIVAR (PATCH /Servicio/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    #@action(detail=True, methods=["patch"], permission_classes = [EsSuperAdministrador])
    def Activar(self, request, pk=None):
        Servicio = ServicioServicio.ObtenerServicioPorId(pk)
        ServicioServicio.ActivarServicio(Servicio)
        return Response({"Mensaje": "Servicio"}, status=status.HTTP_200_OK)

    # ===========================================
    # ELIMINAR (DELETE /Servicio/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    def destroy(self, request, pk=None):
        Servicio = ServicioServicio.ObtenerServicioPorId(pk)
        ServicioServicio.EliminarServicio(Servicio)
        return Response({"Mensaje": "Servicio Eliminado"}, status=status.HTTP_200_OK)