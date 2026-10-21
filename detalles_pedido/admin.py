from django.contrib import admin

from .models import DetallePedido


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ("pk_det_id", "fk_ped", "fk_pla", "det_cantidad", "det_precio")
    search_fields = ("fk_pla__pla_nombre", "det_observacion")
    list_filter = ("fk_pla",)