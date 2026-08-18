from django.db import models

from .ModeloBase import ModeloBase
from .ModeloUsuario import ModeloUsuario
from .ModeloRol import ModeloRol

class ModeloRolUsuario(ModeloBase):

    Id = models.AutoField(db_column='Id', primary_key=True, null=False)
    Usuario = models.ForeignKey(ModeloUsuario, on_delete=models.CASCADE, db_column='Usuario', related_name="RolesUsuario")
    Rol = models.ForeignKey(ModeloRol, on_delete=models.CASCADE, db_column='Rol', related_name="UsuariosRol")

    class Meta:
        db_table = "Rol_Usuario"
        unique_together = (
            "Usuario",
            "Rol"
        )
        verbose_name = "Roles Usuario"
        verbose_name_plural = "Roles Usuarios"
        constraints = [
        models.UniqueConstraint(
            fields=["Usuario", "Rol"],
            name="UniqueUsuarioRol"
        )
    ]