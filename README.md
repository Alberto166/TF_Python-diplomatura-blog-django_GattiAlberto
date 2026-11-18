# Blog Web en Django - Proyecto Final Python

Aplicación web tipo blog desarrollada con **Python** y **Django** como entrega final del curso. Permite a los visitantes leer y buscar publicaciones, y a los usuarios registrados crear, editar y administrar sus propios artículos y perfiles.

## Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Framework Web:** Django
* **Base de Datos:** SQLite3
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Manejo de Imágenes:** Pillow

## Funcionalidades Principales
* **Gestión de Publicaciones (CRUD):** Listado general, vista en detalle, creación, edición y eliminación de posts desde la interfaz web.
* **Carga de Imágenes:** Soporte para subir imágenes en las publicaciones y avatares en los perfiles, con manejo seguro en plantillas cuando un post no posee imagen.
* **Buscador:** Filtrado de publicaciones por palabras clave en el título o contenido.
* **Sistema de Usuarios:** Registro de nuevos usuarios, inicio de sesión (login), cierre de sesión (logout) y visualización/edición de perfil.
* **Rutas Protegidas:** Restricción mediante `@login_required` para que solo usuarios autenticados puedan crear contenido o editar perfiles, y validación de autoría para editar o eliminar publicaciones.

## Instalación y Ejecución Local

Seguí estos pasos para clonar y ejecutar el proyecto desde cero en tu computadora:

### 1. Clonar el repositorio
```bash
git clone <https://github.com/Alberto166/TF_Python-diplomatura-blog-django_GattiAlberto>
cd blog_django
```

### 2. Crear y activar el entorno virtual
* **En Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar las migraciones de la base de datos
Como el repositorio no incluye una base de datos precargada (`db.sqlite3`), ejecutá el siguiente comando para crear las tablas necesarias desde cero:
```bash
python manage.py migrate
```

### 5. (Opcional) Crear un superusuario para el panel administrativo
Si deseás ingresar al panel `/admin` de Django:
```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```
Luego abrí tu navegador e ingresá a `http://127.0.0`.

## Autor
* **Alberto Fabian Gatti** - Proyecto Final del curso de Python.
