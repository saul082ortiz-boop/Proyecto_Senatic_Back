from django.db import models


class ModeloBase(models.Model):

    Estado = models.BooleanField(db_column='Estado', null=False, default=True)
    FechaCreacion = models.DateTimeField(db_column='FechaCreacion', null=False, auto_now_add=True)
    FechaActualizacion = models.DateTimeField(db_column='FechaActualizacion', null=False, auto_now=True)

    class Meta:
        abstract = True