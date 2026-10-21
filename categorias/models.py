from django.db import models


class Categoria(models.Model):
    pk_cat_id = models.AutoField(primary_key=True)
    cat_nombre = models.CharField(max_length=60, unique=True)
    cat_descripcion = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = "tbl_categoria"

    def __str__(self):
        return self.cat_nombre