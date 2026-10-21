from django.db import models


class Pedido(models.Model):
    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("EN_PREPARACION", "En preparación"),
        ("LISTO", "Listo"),
        ("ENTREGADO", "Entregado"),
        ("PAGADO", "Pagado"),
    ]

    pk_ped_id = models.AutoField(primary_key=True)
    fk_mes = models.ForeignKey(
        "mesas.Mesa", on_delete=models.PROTECT, related_name="pedidos"
    )
    fk_mse = models.ForeignKey(
        "meseros.Mesero", on_delete=models.PROTECT, related_name="pedidos"
    )
    ped_fecha = models.DateTimeField(auto_now_add=True)
    ped_estado = models.CharField(max_length=20, choices=ESTADOS, default="PENDIENTE")
    ped_platos = models.ManyToManyField(
        "platos.Plato", through="detalles_pedido.DetallePedido", related_name="pedidos"
    )

    class Meta:
        db_table = "tbl_pedido"

    def __str__(self):
        return f"Pedido #{self.pk_ped_id} - {self.fk_mes}"