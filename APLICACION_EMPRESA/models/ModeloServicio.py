from django.db import models

from APLICACION_USUARIOS.models import ModeloBase

class ModeloServicio(ModeloBase):

    Id = models.AutoField(db_column='Id', primary_key=True, null=False)
    Nombre = models.CharField(db_column='Nombre', max_length=150, unique=True)

    class Meta:
        db_table = "Servicio"
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["Nombre"]

    def __str__(self):
        return self.Nombre