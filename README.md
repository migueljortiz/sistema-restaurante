# Sistema de Pedidos de Restaurante

Proyecto Django del segundo corte de Ingeniería de Sistemas (Uniguajira).

Sistema para registrar los pedidos de un restaurante. Permite gestionar el menú organizado por categorías, las mesas, los meseros y los pedidos de cada mesa con los platos solicitados, sus cantidades y el pago. Toda la información se registra desde el panel de administración de Django.

## Integrantes
- Miguel Ortiz
- Adrian Pimienta
- Josep Romero

## Actores y casos de uso

| Actor | Casos de uso |
|---|---|
| Administrador | Gestionar menú, gestionar mesas, gestionar meseros, consultar reporte de ventas |
| Mesero | Registrar pedido, actualizar pedido, consultar menú, consultar mesas |
| Cocinero | Consultar pedidos pendientes, actualizar estado del pedido, consultar observaciones del pedido |
| Cajero | Consultar cuenta del pedido, registrar pago, consultar historial de pagos |

Diagrama: `docs/diagrama_actores.png`

## Modelo de datos

Diagrama: `docs/diagrama_er.png`

| App | Tabla | Descripción |
|---|---|---|
| categorias | tbl_categoria | Categorías del menú |
| platos | tbl_plato | Platos del menú (relación 1:N con categoría) |
| mesas | tbl_mesa | Mesas del restaurante |
| meseros | tbl_mesero | Meseros |
| pedidos | tbl_pedido | Pedido de una mesa atendido por un mesero |
| detalles_pedido | tbl_detalle_pedido | Tabla intermedia N:M entre pedido y plato (cantidad, observación, precio) |
| pagos | tbl_pago | Pago de un pedido (relación 1:1) |

## Cómo ejecutarlo

```bash
git clone <URL-DEL-REPOSITORIO>
cd <nombre-de-la-carpeta>

python -m venv env
env\Scripts\activate

pip install -r requirements.txt
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/admin/

La base de datos `db.sqlite3` ya incluye los datos de prueba, así que no hace falta ejecutar migraciones.

## Credenciales del superusuario

- Usuario: `migueljortiz`
- Contraseña: `MJOD1996`

## Estructura del proyecto

```
mi_proyecto/
├── taller/            # settings.py, urls.py
├── categorias/        # modelo Categoria
├── platos/            # modelo Plato
├── mesas/             # modelo Mesa
├── meseros/           # modelo Mesero
├── pedidos/           # modelo Pedido
├── detalles_pedido/   # modelo DetallePedido (tabla intermedia del N:M)
├── pagos/             # modelo Pago
├── docs/              # diagramas
├── manage.py
├── requirements.txt
└── README.md
```