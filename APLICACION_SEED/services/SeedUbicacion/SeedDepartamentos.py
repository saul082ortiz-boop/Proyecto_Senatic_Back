import json
from pathlib import Path

from APLICACION_EMPRESA.models import ModeloDepartamento

from APLICACION_SEED.services.BaseSeed import BaseSeed


class SeedDepartamentos(BaseSeed):

    Nombre = "DEPARTAMENTOS"

    @classmethod
    def Crear(cls, Config):
        Ruta = (Path(__file__).resolve().parents[2] / "Data" / "Departamentos.json")
        with open(Ruta, encoding="utf8") as Archivo:
            Departamentos = json.load(Archivo)
        for Departamento in Departamentos:
            cls.CrearSiNoExiste(ModeloDepartamento, Nombre=Departamento["Nombre"], Codigo=Departamento["Codigo"])