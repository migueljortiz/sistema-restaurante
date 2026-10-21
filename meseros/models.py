from django.db import models


class Mesero(models.Model):
    pk_mse_id = models.AutoField(primary_key=True)
    mse_nombre = models.CharField(max_length=60)
    mse_apellido = models.CharField(max_length=60)
    mse_telefono = models.CharField(max_length=20, blank=True)
    mse_activo = models.BooleanField(default=True)

    class Meta:
        db_table = "tbl_mesero"

    def __str__(self):
        return f"{self.mse_nombre} {self.mse_apellido}"