# Sistema de Gestión de Mantención Industrial (API RESTful)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Django](https://img.shields.io/badge/Django-5.0%2B-green) ![DRF](https://img.shields.io/badge/DRF-3.14%2B-red) ![Status](https://img.shields.io/badge/Status-Activo-success)

Backend profesional para la gestión de empresas, equipos técnicos y órdenes de trabajo de mantenimiento. Desarrollado como parte de la Evaluación 4 (TI3041).

## 🚀 Características "Nivel 10"
*   **API RESTful Completa:** CRUD para Empresas, Equipos, Técnicos, Planes y Órdenes.
*   **Documentación Interactiva:** Swagger/OpenAPI autogenerado en español.
*   **Seguridad:** Autenticación JWT con rotación de tokens y permisos granulares.
*   **Optimización:** Consultas SQL optimizadas (`select_related`) y filtros avanzados.
*   **Arquitectura:** Estructura modular y escalable.

## 🛠️ Requisitos del Sistema
*   Python 3.10 o superior
*   Pip (Gestor de paquetes)
*   Git

## 🔧 Instalación y Puesta en Marcha

Sigue estos pasos para levantar el proyecto localmente:

### 1. Clonar el Repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd backend_final
```

### 2. Crear y Activar Entorno Virtual
```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos
```bash
python manage.py migrate
```

### 5. Crear Superusuario (Administrador)
```bash
python manage.py createsuperuser
# Sigue las instrucciones en pantalla
```

### 6. Iniciar el Servidor
```bash
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000/`

## 📚 Documentación de la API

El proyecto cuenta con documentación viva. Una vez iniciado el servidor, visita:

*   **Swagger UI (Recomendado):** [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
    *   Prueba los endpoints directamente desde el navegador.
*   **ReDoc:** [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)

## 🧪 Endpoints Principales

| Recurso | Ruta API | Descripción |
| :--- | :--- | :--- |
| **Auth** | `/api/auth/login/` | Obtener Token JWT |
| **Empresas** | `/api/v1/empresas/` | Gestión de Clientes |
| **Equipos** | `/api/v1/equipos/` | Inventario de Máquinas |
| **Técnicos** | `/api/v1/tecnicos/` | Perfiles de Staff |
| **Órdenes** | `/api/v1/ordenes-trabajo/` | Gestión de flujos de trabajo |

## 👥 Autores
*   **Nombre del Estudiante** - *Desarrollador Backend*

---
*Desarrollado para Inacap - Primavera 2025*
