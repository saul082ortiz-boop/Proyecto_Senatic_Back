import time

from django.core.management.color import color_style

from APLICACION_SEED.services.SeedStatistics import SeedStatistics


Estilo = color_style()

class SeedLogger:

    COLOR_RESET = "\033[0m"
    NEGRO = "\033[30m"
    ROJO = "\033[31m"
    VERDE = "\033[32m"
    AMARILLO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"

    _Inicio = None

    @classmethod
    def Iniciar(cls):
        cls._Inicio = time.perf_counter()
        print(Estilo.HTTP_REDIRECT("╔" + "═" * 78 + "╗"))
        print(Estilo.HTTP_REDIRECT("║" + "SISTEMA DE GENERACIÓN DE DATOS".center(78) + "║"))
        print(Estilo.HTTP_REDIRECT("╚" + "═" * 78 + "╝"))
        print()
    
    @classmethod
    def Finalizar(cls):
        Tiempo = time.perf_counter() - cls._Inicio
        print(Estilo.HTTP_REDIRECT("╔" + "═" * 78 + "╗"))
        print(Estilo.HTTP_REDIRECT("║" + f"PROCESO TERMINADO CORRECTAMENTE EN {Tiempo:.2f} SEGUNDOS".center(78) + "║"))
        print(Estilo.HTTP_REDIRECT("╚" + "═" * 78 + "╝"))


    @classmethod
    def Info(cls, Mensaje):
        print(cls.AZUL + "[INFO] " + cls.COLOR_RESET + Mensaje)


    @classmethod
    def Success(cls, Mensaje):
        print(cls.VERDE +"[OK]   " + cls.COLOR_RESET + Mensaje)

    @classmethod
    def Warning(cls, Mensaje):
        print(cls.AMARILLO +"[WARN] " +cls.COLOR_RESET + Mensaje)

    @classmethod
    def Error(cls, Mensaje):
        print(cls.ROJO +"[ERROR]" + cls.COLOR_RESET + Mensaje)

    @classmethod
    def Titulo(cls, Titulo):
        print(Estilo.HTTP_SERVER_ERROR("╔" + "═" * 78 + "╗"))
        print(Estilo.HTTP_SERVER_ERROR("║" + Titulo.upper().center(78) + "║"))
        print(Estilo.HTTP_SERVER_ERROR("╚" + "═" * 78 + "╝"))

    @classmethod
    def Contador(cls, Nombre, Valor):
        print(Estilo.SUCCESS(f"✔  {Nombre:.<25}{Valor:>5}"))

    @classmethod
    def ContadorResumenGeneral(cls, Nombre, Valor):
        Contenido = f"     ✔  {Nombre:.<25}{Valor:>5}"
        print(Estilo.HTTP_SERVER_ERROR("║") + Estilo.WARNING(f"{Contenido:<78}") + Estilo.HTTP_SERVER_ERROR("║"))

    @classmethod
    def MostrarModulo(cls, Nombre):
        Datos = SeedStatistics.Estadisticas[Nombre]
        cls.Contador("CREADOS", Datos["Creados"])
        cls.Contador("ACTUALIZADOS", Datos["Actualizados"])
        cls.Contador("EXISTENTES", Datos["Existentes"])
        cls.Contador("ELIMINADOS", Datos["Eliminados"])
        print(Estilo.HTTP_INFO(f"TIEMPO: {Datos['Tiempo']:.2f} SEGUNDOS"))
        print()

    @classmethod
    def ResumenGeneral(cls, Estadisticas):
        print()
        print()
        print(Estilo.WARNING("╔" + "═" * 78 + "╗"))
        print(Estilo.WARNING("║" + "RESUMEN GENERAL".center(78) + "║"))
        print(Estilo.WARNING("╚" + "═" * 78 + "╝"))
        print()

        TotalCreados = 0
        TotalActualizados = 0
        TotalExistentes = 0
        TotalEliminados = 0
        TiempoTotal = 0

        for Modulo, Datos in Estadisticas.items():
            print(Estilo.WARNING(Modulo.upper()))
            cls.Contador("CREADOS", Datos["Creados"])
            cls.Contador("ACTUALIZADOS", Datos["Actualizados"])
            cls.Contador("EXISTENTES", Datos["Existentes"])
            cls.Contador("ELIMINADOS", Datos["Eliminados"])
            print(Estilo.HTTP_INFO(f"TIEMPO: {Datos['Tiempo']:.2f} SEGUNDOS"))
            print()

            TotalCreados += Datos["Creados"]
            TotalActualizados += Datos["Actualizados"]
            TotalExistentes += Datos["Existentes"]
            TotalEliminados += Datos["Eliminados"]
            TiempoTotal += Datos["Tiempo"]

        print(Estilo.HTTP_SERVER_ERROR("╔" + "═" * 78 + "╗"))
        cls.ContadorResumenGeneral("TOTAL CREADOS", TotalCreados)
        cls.ContadorResumenGeneral("TOTAL ACTUALIZADOS", TotalActualizados)
        cls.ContadorResumenGeneral("TOTAL EXISTENTES", TotalExistentes)
        cls.ContadorResumenGeneral("TOTAL ELIMINADOS", TotalEliminados)
        Contenido = f"     TIEMPO TOTAL: {TiempoTotal:.2f} SEGUNDOS"
        print(Estilo.HTTP_SERVER_ERROR("║") + Estilo.HTTP_INFO(f"{Contenido:<78}") + Estilo.HTTP_SERVER_ERROR("║"))
        print(Estilo.HTTP_SERVER_ERROR("╚" + "═" * 78 + "╝"))

    @classmethod
    def Grupo(cls, Nombre):
        print(Estilo.MIGRATE_HEADING("╔" + "═" * 78 + "╗"))
        print(Estilo.MIGRATE_HEADING(f"║{Nombre.center(78)}║"))
        print(Estilo.MIGRATE_HEADING("╚" + "═" * 78 + "╝"))
        print()