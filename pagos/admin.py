from django.contrib import admin

from .models import Pago


class PagoInline(admin.StackedInline):
    model = Pago
    extra = 0
    max_num = 1


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("pk_pag_id", "fk_ped", "pag_fecha", "pag_monto", "pag_metodo")
    search_fields = ("fk_ped__pk_ped_id",)
    list_filter = ("pag_metodo", "pag_fecha")