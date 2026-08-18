from django.db import transaction

from APLICACION_EMPRESA.models import ModeloEmpresa, ModeloServicioEmpresa
from APLICACION_USUARIOS.models import ModeloRolUsuario, ModeloUsuario, ModeloRol, ModeloTipoIdentificacion
from APLICACION_EMPRESA.models import ModeloServicio, ModeloTipoEmpresa, ModeloMunicipio, ModeloDepartamento
from .SeedLogger import SeedLogger


class SeedCleaner:

    @classmethod
    @transaction.atomic
    def Ejecutar(cls):
        SeedLogger.Info("Eliminando datos de prueba...")
        ModeloServicioEmpresa.objects.all().delete()
        ModeloEmpresa.objects.all().delete()
        ModeloUsuario.objects.all().delete()
        ModeloRolUsuario.objects.all().delete()
        ModeloServicio.objects.all().delete()
        ModeloTipoEmpresa.objects.all().delete()
        ModeloRol.objects.all().delete()
        ModeloTipoIdentificacion.objects.all().delete()
        ModeloMunicipio.objects.all().delete()
        ModeloDepartamento.objects.all().delete()
        SeedLogger.Success("Base de datos limpia.")