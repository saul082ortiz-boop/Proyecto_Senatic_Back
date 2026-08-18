from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)

from .ModeloBase import ModeloBase
from .ModeloTipoIdentificacion import ModeloTipoIdentificacion
from .UsuarioManager import UsuarioManager

class ModeloUsuario(AbstractBaseUser, PermissionsMixin, ModeloBase):

    Id = models.AutoField(db_column='Id', primary_key=True, null=False)
    Nombre = models.CharField(db_column='Nombre', max_length=100)
    Apellido = models.CharField(db_column='Apellido', max_length=100)
    Telefono = models.CharField(db_column='Telefono', max_length=20)
    NumeroIdentificacion = models.CharField(db_column='NumeroIdentificacion', max_length=20, unique=True)
    TipoIdentificacion = models.ForeignKey(ModeloTipoIdentificacion, on_delete=models.PROTECT, db_column='TipoIdentificacion')
    Correo = models.EmailField(db_column='Correo', max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "Correo"

    REQUIRED_FIELDS = [
        "Nombre",
        "Apellido",
        "Telefono",
        "NumeroIdentificacion",
        "TipoIdentificacion"
    ]

    class Meta:
        db_table = "Usuario"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.Nombre

    objects = UsuarioManager()

    def TieneRol(self, Nombre_Rol: str) -> bool:
        return self.RolesUsuario.filter(Rol__Nombre=Nombre_Rol, Estado=True).exists()