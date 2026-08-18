import time

class SeedStatistics:

    Estadisticas = {}

    @classmethod
    def Reiniciar(cls):
        cls.Estadisticas = {}

    @classmethod
    def IniciarModulo(cls, Nombre):
        cls.Estadisticas[Nombre] = {
            "Creados": 0,
            "Actualizados": 0,
            "Existentes": 0,
            "Eliminados": 0,
            "Inicio": time.perf_counter(),
            "Tiempo": 0
        }

    @classmethod
    def FinalizarModulo(cls, Nombre):
        Modulo = cls.Estadisticas[Nombre]
        Modulo["Tiempo"] = round((time.perf_counter() - Modulo["Inicio"]), 2)

    @classmethod
    def Incrementar(cls, Modulo, Tipo):
        cls.Estadisticas[Modulo][Tipo] += 1

    @classmethod
    def ObtenerModulo(cls, Nombre):
        return cls.Estadisticas[Nombre]

    @classmethod
    def ObtenerTodos(cls):
        return cls.Estadisticas
