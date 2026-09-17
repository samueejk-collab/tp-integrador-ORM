# biblioteca-orm
## Integrantes
* **Samuel Huallpa** 
## Estructura del Proyecto
* `schema.py`: Definición de los modelos de la base de datos (Autor, Libro, Socio, Prestamo) y configuración del Engine.
* `seed.py`: Población inicial de la base de datos con un mínimo de 10 registros por tabla de manera coherente.
* `consultas.py`: Scripts de consulta utilizando filtros avanzados, operadores lógicos y ordenamiento.

## Instrucciones para Correr el Proyecto

### 1. Requisitos Previos
Tener instalado Python 3.x y el gestor de paquetes `pip`.

### 2. Instalación de Dependencias
Instalar SQLAlchemy ejecutando el siguiente comando en la terminal:
```bash
pip install sqlalchemy
```
### 3. Ejecución del Proyecto
Para inicializar la base de datos y probar las consultas, ejecutar los scripts en el siguiente orden estricto:

1. **Crear e inicializar las tablas:**
   ```bash
   python schema.py
   ```
2. **Poblar la base de datos con datos de prueba:**
   ```bash
   python seed.py
   ```
3. **Ejecutar y ver las consultas en consola:**
   ```bash
   python consultas.py
   ```
