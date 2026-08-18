import random

from django.db import transaction

from .SeedLogger import SeedLogger
from .SeedStatistics import SeedStatistics

class BaseSeed:

    Nombre = ""

    @classmethod
    def Ejecutar(cls, Config):
        SeedLogger.Titulo(cls.Nombre)
        SeedStatistics.IniciarModulo(cls.Nombre)
        with transaction.atomic():
            cls.Crear(Config)
        SeedStatistics.FinalizarModulo(cls.Nombre)
        SeedLogger.MostrarModulo(cls.Nombre)

    @classmethod
    def Crear(cls, Config):
        raise NotImplementedError()

    @classmethod
    def CrearSiNoExiste(cls, Modelo, **kwargs):
        Objeto, Creado = Modelo.objects.get_or_create(**kwargs)
        if Creado:
            SeedStatistics.Incrementar(cls.Nombre, "Creados")
        else:
            SeedStatistics.Incrementar(cls.Nombre, "Existentes")
        return Objeto, Creado

    @classmethod
    def ActualizarOCrear(cls, Modelo, defaults=None, **kwargs):
        Objeto, Creado = Modelo.objects.update_or_create(defaults=defaults or {}, **kwargs)
        if Creado:
            SeedStatistics.Incrementar(cls.Nombre, "Creados")
        else:
            SeedStatistics.Incrementar(cls.Nombre, "Actualizados")
        return Objeto

    @classmethod
    def ObtenerAleatorio(Modelo):
        Cantidad = Modelo.objects.count()
        if Cantidad == 0:
            return None
        Indice = random.randint(0, Cantidad - 1)
        return Modelo.objects.all()[Indice]

    @classmethod
    def ObtenerMuchosAleatorios(Modelo, Cantidad):
        Ids = list(Modelo.objects.values_list("pk", flat=True))
        random.shuffle(Ids)
        return Modelo.objects.filter(pk__in=Ids[:Cantidad])

    @classmethod
    def MostrarCantidad(Modelo):
        SeedLogger.Info(f"{Modelo.__name__}: {Modelo.objects.count()} Registros")

    @classmethod
    def LimpiarTabla(Modelo):
        Modelo.objects.all().delete()

    @classmethod
    def EliminarTodo(cls, Modelo):
        Cantidad = Modelo.objects.count()
        Modelo.objects.all().delete()
        SeedStatistics.Incrementar(cls.Nombre, Cantidad)