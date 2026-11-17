from django import forms
from django.forms import inlineformset_factory

from detalles_pedido.models import DetallePedido

from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["fk_mes", "fk_mse", "ped_estado"]
        labels = {
            "fk_mes": "Mesa",
            "fk_mse": "Mesero",
            "ped_estado": "Estado",
        }
        widgets = {
            "fk_mes": forms.Select(attrs={"class": "form-select"}),
            "fk_mse": forms.Select(attrs={"class": "form-select"}),
            "ped_estado": forms.Select(attrs={"class": "form-select"}),
        }


DetalleFormSet = inlineformset_factory(
    Pedido,
    DetallePedido,
    fields=["fk_pla", "det_cantidad", "det_observacion", "det_precio"],
    labels={
        "fk_pla": "Plato",
        "det_cantidad": "Cantidad",
        "det_observacion": "Observación",
        "det_precio": "Precio unitario",
    },
    widgets={
        "fk_pla": forms.Select(attrs={"class": "form-select"}),
        "det_cantidad": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        "det_observacion": forms.TextInput(attrs={"class": "form-control"}),
        "det_precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
    },
    extra=3,
    min_num=1,
    validate_min=True,
    can_delete=True,
)