from django.contrib import admin

from .models import Mesa


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ("pk_mes_id", "mes_numero", "mes_capacidad", "mes_ubicacion")
    search_fields = ("mes_numero", "mes_ubicacion")
    list_filter = ("mes_ubicacion", "mes_capacidad")