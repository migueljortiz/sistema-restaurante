from django.contrib import admin

from .models import Plato


@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ("pk_pla_id", "pla_nombre", "fk_cat", "pla_precio", "pla_disponible")
    search_fields = ("pla_nombre", "pla_descripcion", "fk_cat__cat_nombre")
    list_filter = ("fk_cat", "pla_disponible")