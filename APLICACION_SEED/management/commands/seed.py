from django.core.management.base import BaseCommand

from APLICACION_SEED.services.SeedConfig import SeedConfig
from APLICACION_SEED.services.ServicioSeed import ServicioSeed


class Command(BaseCommand):

    help = "Genera datos de prueba para el sistema"

    def add_arguments(self, parser):
        parser.add_argument("--Clear", action="store_true", help="Elimina los datos antes de generarlos")

        parser.add_argument("--Module", type=str, 
            choices=[
                "Catalogos",
                "Ubicacion",
                "Usuarios",
                "Empresa",
                "All"
            ], default="All", help="Módulo a ejecutar"
        )
        parser.add_argument("--Users", type=int, default=50, help="Cantidad de usuarios")
        parser.add_argument("--Companies", type=int, default=20, help="Cantidad de empresas")

    def handle(self, *args, **options):
        Config = SeedConfig()
        Config.Limpiar = options["Clear"]
        Config.Modulo = options["Module"]
        Config.CantidadUsuarios = options["Users"]
        Config.CantidadEmpresas = options["Companies"]
        ServicioSeed.Ejecutar(Config)
