from django.db import models

from .ModeloBase import ModeloBase


class ModeloRol(ModeloBase):

    Id = models.AutoField(db_column='Id', primary_key=True, null=False)
    Nombre = models.CharField(db_column='Nombre', max_length=100, unique=True)

    class Meta:
        db_table = "Rol"
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.Nombre