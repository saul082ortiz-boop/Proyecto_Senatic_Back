from django.db import transaction

from APLICACION_SEED.services import ModuloSeed, SeedLogger
from APLICACION_SEED.services import SeedStatistics

from .SeedCleaner import SeedCleaner

from APLICACION_SEED.services.SeedCatalogos import SeedCatalogos
from APLICACION_SEED.services.SeedUbicacion import SeedUbicacion
from APLICACION_SEED.services.SeedUsuarios import SeedUsuarios
from APLICACION_SEED.services.SeedEmpresas import SeedEmpresas

class ServicioSeed:

    MODULOS = {
        "Catalogos": ModuloSeed(SeedCatalogos, []),
        "Ubicacion": ModuloSeed(SeedUbicacion, []),
        "Usuarios": ModuloSeed(SeedUsuarios, ["Catalogos"]),
        "Empresa": ModuloSeed(SeedEmpresas, ["Catalogos", "Ubicacion", "Usuarios"]),
    }

    Ejecutados = set()

    @classmethod
    def Ejecutar(cls, Config):
        with transaction.atomic():
            SeedStatistics.Reiniciar()
            SeedLogger.Iniciar()
            cls.Ejecutados.clear()

            if Config.Limpiar:
                SeedCleaner.Ejecutar()
                return

            if Config.Modulo not in cls.MODULOS and Config.Modulo != "All":
                raise ValueError(f"El módulo '{Config.Modulo}' no existe.")

            if Config.Modulo == "All":
                for NombreModulo in cls.MODULOS.keys():
                    cls.EjecutarModulo(NombreModulo, Config)
            else:
                cls.EjecutarModulo(Config.Modulo, Config)

            SeedLogger.ResumenGeneral(SeedStatistics.ObtenerTodos())
            SeedLogger.Finalizar()

    @classmethod
    def EjecutarModulo(cls, NombreModulo, Config):
        if NombreModulo in cls.Ejecutados:
            return
        Modulo = cls.MODULOS[NombreModulo]
        for Dependencia in Modulo.Dependencias:
            cls.EjecutarModulo(Dependencia, Config)
        Modulo.Clase.Ejecutar(Config)
        cls.Ejecutados.add(NombreModulo)