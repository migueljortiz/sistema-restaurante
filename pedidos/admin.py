from django.contrib import admin

from detalles_pedido.admin import DetallePedidoInline
from pagos.admin import PagoInline

from .models import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("pk_ped_id", "fk_mes", "fk_mse", "ped_fecha", "ped_estado")
    search_fields = ("pk_ped_id", "fk_mse__mse_nombre", "fk_mse__mse_apellido")
    list_filter = ("ped_estado", "fk_mes", "fk_mse")
    inlines = [DetallePedidoInline, PagoInline]