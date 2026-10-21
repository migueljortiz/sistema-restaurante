from django.contrib import admin

from .models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("pk_cat_id", "cat_nombre", "cat_descripcion")
    search_fields = ("cat_nombre", "cat_descripcion")
    list_filter = ("cat_nombre",)