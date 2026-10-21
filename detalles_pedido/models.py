from django.db import models


class DetallePedido(models.Model):
    pk_det_id = models.AutoField(primary_key=True)
    fk_ped = models.ForeignKey(
        "pedidos.Pedido", on_delete=models.CASCADE, related_name="detalles"
    )
    fk_pla = models.ForeignKey(
        "platos.Plato", on_delete=models.PROTECT, related_name="detalles"
    )
    det_cantidad = models.PositiveIntegerField(default=1)
    det_observacion = models.CharField(max_length=200, blank=True)
    det_precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "tbl_detalle_pedido"

    def __str__(self):
        return f"{self.det_cantidad} x {self.fk_pla.pla_nombre}"