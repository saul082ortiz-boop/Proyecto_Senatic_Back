import json
from pathlib import Path

from APLICACION_EMPRESA.models import ModeloDepartamento, ModeloMunicipio

from APLICACION_SEED.services.BaseSeed import BaseSeed


class SeedMunicipios(BaseSeed):

    Nombre = "MUNICIPIOS"

    @classmethod
    def Crear(cls, Config):
        Ruta = (Path(__file__).resolve().parents[2] / "Data" / "Municipios.json")
        with open(Ruta, encoding="utf8") as Archivo:
            Municipios = json.load(Archivo)

        for Municipio in Municipios:
            Departamento = ModeloDepartamento.objects.get(Codigo=Municipio["Departamento"])
            cls.CrearSiNoExiste(ModeloMunicipio, Nombre=Municipio["Nombre"], Departamento=Departamento, Codigo=Municipio["Codigo"])