from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated

from APLICACION_EMPRESA.models import ModeloDepartamento
from APLICACION_EMPRESA.serializers.read.Departamento import SerializadorDetalleDepartamento, SerializadorListaDepartamento
from APLICACION_EMPRESA.serializers.write.Departamento import SerializadorActualizarDepartamento, SerializadorCrearDepartamento
from APLICACION_EMPRESA.services import ServicioDepartamento
from APLICACION_USUARIOS.serializers.common import SerializadorVacio

class VistasDepartamento(
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
            return SerializadorListaDepartamento
        if self.action == "retrieve":
            return SerializadorDetalleDepartamento
        if self.action == "create":
            return SerializadorCrearDepartamento
        if self.action == "update":
            return SerializadorActualizarDepartamento
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

    queryset = ModeloDepartamento.objects.all()

    # ===========================================
    # LISTAR (GET /departamento/)
    # ===========================================
    def list(self, request):
        Departamentos = ServicioDepartamento.ObtenerDepartamentos()
        Serializador = SerializadorListaDepartamento(Departamentos, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # OBTENER (GET /departamento/{id}/)
    # ===========================================
    def retrieve(self, request, pk=None):
        Departamento = ServicioDepartamento.ObtenerDepartamentoPorId(pk)
        Serializador = SerializadorDetalleDepartamento(Departamento)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # CREAR (POST /departamento/)
    # ===========================================
    def create(self, request):
        Serializador = SerializadorCrearDepartamento(data=request.data)
        Serializador.is_valid(raise_exception=True)
        Departamento = ServicioDepartamento.CrearDepartamento(Serializador.validated_data)
        SerializadorRespuesta = SerializadorDetalleDepartamento(Departamento)
        return Response(SerializadorRespuesta.data, status=status.HTTP_201_CREATED)

    # ===========================================
    # ACTUALIZAR COMPLETO (PUT /departamento/{id}/)
    # ===========================================
    def update(self, request, pk=None):
        Departamento = ServicioDepartamento.ObtenerDepartamentoPorId(pk)
        Serializador = SerializadorActualizarDepartamento(Departamento, data=request.data)
        Serializador.is_valid(raise_exception=True)
        Departamento = ServicioDepartamento.ActualizarDepartamento(Departamento,Serializador.validated_data)
        return Response(SerializadorDetalleDepartamento(Departamento).data, status=status.HTTP_200_OK)

    # ===========================================
    # ACTIVAR (PATCH /departamento/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    #@action(detail=True, methods=["patch"], permission_classes = [EsSuperAdministrador])
    def Activar(self, request, pk=None):
        Departamento = ServicioDepartamento.ObtenerDepartamentoPorId(pk)
        ServicioDepartamento.ActivarDepartamento(Departamento)
        return Response({"Mensaje": "Departamento"}, status=status.HTTP_200_OK)

    # ===========================================
    # ELIMINAR (DELETE /departamento/{id}/)
    # ===========================================
    @extend_schema(request=None, responses={200: None})
    def destroy(self, request, pk=None):
        Departamento = ServicioDepartamento.ObtenerDepartamentoPorId(pk)
        ServicioDepartamento.EliminarDepartamento(Departamento)
        return Response({"Mensaje": "Departamento Eliminado"}, status=status.HTTP_200_OK)