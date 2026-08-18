from dataclasses import dataclass

@dataclass
class SeedConfig:

    Limpiar: bool = False
    Modulo: str = "All"

    # Cantidades
    CantidadUsuarios: int = 70
    CantidadAdministradoresEmpresa: int = 25
    CantidadSuperAdmin: int = 5
    CantidadEmpresas: int = 50

    # Futuras entidades
    CantidadReservas: int = 100
    CantidadHorarios: int = 50
    CantidadDisponibilidades: int = 100