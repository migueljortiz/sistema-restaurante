from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DetalleFormSet, PedidoForm
from .models import Pedido


def lista(request):
    pedidos = (
        Pedido.objects
        .select_related("fk_mes", "fk_mse")
        .order_by("-ped_fecha")
    )
    return render(request, "pedidos/lista.html", {"pedidos": pedidos})


def crear(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        formset = DetalleFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                pedido = form.save()
                formset.instance = pedido
                formset.save()
            messages.success(request, "Pedido registrado correctamente.")
            return redirect("pedidos:lista")
    else:
        form = PedidoForm()
        formset = DetalleFormSet()
    return render(
        request,
        "pedidos/formulario.html",
        {"form": form, "formset": formset, "titulo": "Nuevo pedido"},
    )

def editar(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        formset = DetalleFormSet(request.POST, instance=pedido)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form.save()
                formset.save()
            messages.success(request, "Pedido actualizado correctamente.")
            return redirect("pedidos:lista")
    else:
        form = PedidoForm(instance=pedido)
        formset = DetalleFormSet(instance=pedido)
    return render(
        request,
        "pedidos/formulario.html",
        {"form": form, "formset": formset, "titulo": f"Editar pedido #{pedido.pk_ped_id}"},
    )

def eliminar(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        pedido.delete()
        messages.success(request, f"Pedido #{pk} eliminado correctamente.")
        return redirect("pedidos:lista")
    return render(request, "pedidos/confirmar_eliminar.html", {"pedido": pedido})