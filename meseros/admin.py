from django.contrib import admin

from .models import Mesero


@admin.register(Mesero)
class MeseroAdmin(admin.ModelAdmin):
    list_display = ("pk_mse_id", "mse_nombre", "mse_apellido", "mse_telefono", "mse_activo")
    search_fields = ("mse_nombre", "mse_apellido", "mse_telefono")
    list_filter = ("mse_activo",)