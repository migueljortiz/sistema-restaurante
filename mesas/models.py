from django.db import models


class Mesa(models.Model):
    pk_mes_id = models.AutoField(primary_key=True)
    mes_numero = models.PositiveIntegerField(unique=True)
    mes_capacidad = models.PositiveIntegerField()
    mes_ubicacion = models.CharField(max_length=60, blank=True)

    class Meta:
        db_table = "tbl_mesa"

    def __str__(self):
        return f"Mesa {self.mes_numero}"