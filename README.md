# Sistema de Pedidos de Restaurante

## Descripción
Sistema web para registrar los pedidos de un restaurante. Permite manejar el menú organizado por categorías, las mesas, los meseros y los pedidos de cada mesa con los platos solicitados, sus cantidades y su pago. Está pensado para el personal del restaurante: administrador, mesero, cocinero y cajero.

## Integrantes
- Miguel Ortiz – migueljortiz
- Adrian Pimienta – yeimerpimienta
- Josep Romero – joshepdavid987

## Tecnologías
- Django 6.1.2
- Python 3.13
- Bootstrap 5.3.3, incluido por CDN en `templates/base.html` (hoja de estilos y script desde cdn.jsdelivr.net)
- SQLite como base de datos

## Tablas principales
| Tabla | Descripción |
| --- | --- |
| tbl_categoria | Categorías del menú |
| tbl_plato | Platos del menú (relación 1:N con categoría) |
| tbl_mesa | Mesas del restaurante |
| tbl_mesero | Meseros |
| tbl_pedido | Pedido de una mesa atendido por un mesero |
| tbl_detalle_pedido | Tabla intermedia N:M entre pedido y plato (cantidad, observación, precio); entidad débil de pedido |
| tbl_pago | Pago de un pedido (relación 1:1) |

## Diagramas
- Actores: docs/diagrama_actores.png
- Entidad-relación: docs/diagrama_er.png

## Funcionalidades
- **CRUD completo de pedidos** (mesa, mesero y platos con cantidad), con página propia para cada acción:
  - Listar: `/`
  - Crear: `/nuevo/`
  - Editar: `/<id>/editar/`
  - Eliminar (con confirmación): `/<id>/eliminar/`
- Mensajes de confirmación después de guardar, actualizar o eliminar.
- Plantilla base con barra de navegación, menú lateral, tarjetas y pie de página.
- El panel de administración sigue funcionando en `/admin/`.

## Cómo ejecutar el proyecto
1. git clone https://github.com/migueljortiz/sistema-restaurante.git
2. python -m venv env
3. env\Scripts\activate   (Linux/macOS: source env/bin/activate)
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py runserver

Abrir en el navegador: http://127.0.0.1:8000/

## Usuarios de prueba
- Superusuario del admin: usuario `migueljortiz`, contraseña `MJOD1996`