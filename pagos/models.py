from django.db import models


class Pago(models.Model):
    METODOS = [
        ("EFECTIVO", "Efectivo"),
        ("TARJETA", "Tarjeta"),
        ("TRANSFERENCIA", "Transferencia"),
    ]

    pk_pag_id = models.AutoField(primary_key=True)
    fk_ped = models.OneToOneField(
        "pedidos.Pedido", on_delete=models.CASCADE, related_name="pago"
    )
    pag_fecha = models.DateTimeField(auto_now_add=True)
    pag_monto = models.DecimalField(max_digits=10, decimal_places=2)
    pag_metodo = models.CharField(max_length=20, choices=METODOS, default="EFECTIVO")

    class Meta:
        db_table = "tbl_pago"

    def __str__(self):
        return f"Pago #{self.pk_pag_id} - ${self.pag_monto}"