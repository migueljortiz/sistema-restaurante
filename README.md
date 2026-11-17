
# Sistema de Pedidos de Restaurante

## Descripción

Sistema web desarrollado con Django para registrar y administrar los pedidos de un restaurante. Permite manejar el menú organizado por categorías, las mesas, los meseros y los pedidos de cada mesa con sus platos, cantidades y pagos.

Está pensado para el personal del restaurante: administrador, mesero, cocinero y cajero.

En el tercer corte se implementó una interfaz gráfica con Bootstrap, un CRUD completo de pedidos y una funcionalidad adicional para consultar los platos registrados en cada pedido.

## Integrantes

- Miguel Ortiz – migueljortiz
- Adrian Pimienta – yeimerpimienta
- Josep Romero – joshepdavid987

## Tecnologías

- Django 6.1.2
- Python 3.13
- Bootstrap 5.3.3, incluido por CDN en `templates/base.html`
- SQLite como base de datos
- HTML y CSS

## Tablas principales

| Tabla | Descripción |
|---|---|
| tbl_categoria | Categorías del menú |
| tbl_plato | Platos del menú (relación 1:N con categoría) |
| tbl_mesa | Mesas del restaurante |
| tbl_mesero | Meseros del restaurante |
| tbl_pedido | Pedido de una mesa atendido por un mesero |
| tbl_detalle_pedido | Tabla intermedia que resuelve la relación N:M entre pedidos y platos, almacenando cantidad, observación y precio |
| tbl_pago | Pago asociado a un pedido (relación 1:0..1) |

## Diagramas

- Diagrama de casos de uso actualizado: `docs/diagrama_actores.png`
- Diagrama de casos de uso del segundo corte: `docs/diagrama_actores_segundo_corte.png`
- Diagrama entidad-relación: `docs/diagrama_er.png`

El diagrama original del segundo corte se conserva para comparar los cambios realizados en el proyecto.

## Funcionalidades

### 1. CRUD completo de pedidos

Se implementó un CRUD completo desde una interfaz web propia desarrollada con Django y Bootstrap.

El sistema permite:

- **Crear:** registrar pedidos seleccionando mesa, mesero, platos y cantidades.
- **Consultar:** visualizar los pedidos registrados con su mesa, mesero, fecha, estado y cantidad de platos diferentes.
- **Actualizar:** modificar los datos de un pedido existente.
- **Eliminar:** eliminar un pedido mediante confirmación previa.

Rutas del CRUD:

| Operación | Ruta |
|---|---|
| Listar pedidos | `/` |
| Crear pedido | `/nuevo/` |
| Editar pedido | `/<id>/editar/` |
| Eliminar pedido | `/<id>/eliminar/` |

### 2. Consulta detallada de pedidos

Se implementó una funcionalidad adicional para consultar la información completa de cada pedido.

En la página de pedidos registrados se agregó una columna llamada **Detalles**, que contiene un ícono de ojo.

Al seleccionar este ícono, el sistema muestra:

- Número del pedido.
- Mesa asignada.
- Mesero responsable.
- Fecha y hora.
- Estado del pedido.
- Nombre de los platos solicitados.
- Cantidad de cada plato.
- Precio unitario.
- Subtotal de cada plato.
- Observaciones.
- Valor total del pedido.

**Ruta:** `/<id>/detalle/`

Esta funcionalidad consulta la información relacionada entre las tablas `tbl_pedido`, `tbl_detalle_pedido` y `tbl_plato`.

El subtotal se calcula multiplicando la cantidad por el precio unitario de cada plato.

El total del pedido se obtiene sumando todos los subtotales.

No fue necesario modificar las tablas de la base de datos.

### 3. Interfaz gráfica

La interfaz fue desarrollada utilizando Bootstrap 5.3.3.

Incluye:

- Barra de navegación superior.
- Menú lateral.
- Tarjetas para organizar el contenido.
- Tablas de pedidos.
- Formularios para registrar y actualizar.
- Botones para editar y eliminar.
- Ícono de ojo para consultar detalles.
- Pie de página.
- Paleta de colores uniforme.

Las páginas utilizan herencia de plantillas mediante `templates/base.html`.

### 4. Validaciones y mensajes

- Validación de formularios mediante Django.
- Mensajes de confirmación al registrar pedidos.
- Mensajes al actualizar pedidos.
- Confirmación antes de eliminar.
- Manejo de pedidos inexistentes mediante error HTTP 404.

### 5. Panel de administración

El panel de administración Django continúa funcionando en:

`/admin/`

Permite gestionar los modelos registrados del sistema.

## Estructura del proyecto

El sistema está organizado en aplicaciones Django.

Aplicaciones principales:

- `categorias/`
- `platos/`
- `mesas/`
- `meseros/`
- `pedidos/`
- `detalles_pedido/`
- `pagos/`

Archivos importantes:

- `models.py`: modelos y relaciones de la base de datos.
- `views.py`: funciones que procesan las solicitudes.
- `urls.py`: rutas del sistema.
- `pedidos/forms.py`: formularios para crear y editar pedidos.
- `templates/base.html`: plantilla base.
- `templates/pedidos/lista.html`: listado de pedidos.
- `templates/pedidos/formulario.html`: creación y edición.
- `templates/pedidos/confirmar_eliminar.html`: confirmación de eliminación.
- `templates/pedidos/detalle.html`: consulta de platos y detalles.
- `docs/`: diagramas del sistema.
- `requirements.txt`: dependencias del proyecto.
- `db.sqlite3`: base de datos SQLite.

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

   `git clone https://github.com/migueljortiz/sistema-restaurante.git`

2. Entrar a la carpeta:

   `cd sistema-restaurante`

3. Crear el entorno virtual:

   `python -m venv env`

4. Activar el entorno virtual:

   Windows: `env\Scripts\activate`

   Linux/macOS: `source env/bin/activate`

5. Instalar dependencias:

   `pip install -r requirements.txt`

6. Aplicar migraciones:

   `python manage.py migrate`

7. Ejecutar el servidor:

   `python manage.py runserver`

8. Abrir en el navegador:

   `http://127.0.0.1:8000/`

## Usuarios de prueba

- Superusuario del administrador: `migueljortiz`
- Acceso al administrador: `/admin/`
- Contraseña: MJOD1996

Por seguridad, no se incluyen contraseñas en el repositorio público.

## Cambios realizados en el tercer corte

Con respecto al segundo corte se implementaron las siguientes mejoras:

1. Interfaz gráfica propia utilizando Bootstrap.
2. CRUD completo de pedidos desde páginas web.
3. Formularios para crear y modificar pedidos.
4. Confirmación antes de eliminar pedidos.
5. Consulta detallada de pedidos mediante un ícono de ojo.
6. Visualización de platos, cantidades, precios, subtotales y total.
7. Actualización del diagrama de casos de uso.
8. Conservación del diagrama original del segundo corte.
9. Actualización de la documentación y del repositorio GitHub.

Se mantuvieron las siete tablas principales y sus relaciones, ya que las mejoras implementadas no requirieron cambios estructurales en la base de datos.
