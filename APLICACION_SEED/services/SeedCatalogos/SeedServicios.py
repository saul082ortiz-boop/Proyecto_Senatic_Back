from APLICACION_EMPRESA.models import ModeloServicio
from APLICACION_SEED.services.BaseSeed import BaseSeed
from ..SeedUtils import SERVICIOS

class SeedServicios(BaseSeed):

    Nombre = "SERVICIOS"

    @classmethod
    def Crear(cls, Config):
        for Servicios in SERVICIOS.values():
            for NombreServicio in Servicios:
                cls.CrearSiNoExiste(ModeloServicio, Nombre=NombreServicio)