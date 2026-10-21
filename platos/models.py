from django.db import models


class Plato(models.Model):
    pk_pla_id = models.AutoField(primary_key=True)
    fk_cat = models.ForeignKey(
        "categorias.Categoria", on_delete=models.PROTECT, related_name="platos"
    )
    pla_nombre = models.CharField(max_length=100)
    pla_descripcion = models.CharField(max_length=250, blank=True)
    pla_precio = models.DecimalField(max_digits=10, decimal_places=2)
    pla_disponible = models.BooleanField(default=True)

    class Meta:
        db_table = "tbl_plato"

    def __str__(self):
        return f"{self.pla_nombre} (${self.pla_precio})"