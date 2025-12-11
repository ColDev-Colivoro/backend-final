# Documentación Completa del Proyecto (TI3041 - Evaluación 4)

Este documento sirve como la **referencia central de trabajo**, consolidando los requerimientos originales y elevando el estándar a un nivel **"Más allá de las expectativas" (Nivel 10/10)**, utilizando estrictamente **ESPAÑOL** para todo el código y estructura.

---

## 🚀 META: Excelencia Superior (Nivel 10/10)
Nuestro objetivo no es solo obtener el puntaje máximo ("Excelente"), sino construir una aplicación profesional, robusta y escalable que supere los requisitos académicos básicos.

### Tabla de Objetivos: De "Excelente" a "Supera Expectativas"

| Criterios | Estándar "Excelente" (Rúbrica) | 🏆 Estándar "Nivel 10" (Nuestro Objetivo) |
| :--- | :--- | :--- |
| **Configuración DRF** | Instala e integra DRF. | ✅ Configuración modular, estructura profesional "cookiecutter", manejo centralizado de excepciones. |
| **Configuración Global** | Configura JSON, API navegable. | ✅ **Swagger/OpenAPI** en español. Paginación estandarizada. |
| **Autenticación** | Token/Session. | ✅ **JWT con rotación (Refresh Tokens)**. Seguridad reforzada. |
| **Control de Acceso** | Restricción básica. | ✅ **Permisos granulares**. `EsDuenioOLectura` para que usuarios solo editen lo suyo. |
| **Modelado** | 5 entidades correctas. | ✅ Modelos con **índices de DB**, constraints (`CheckConstraints`), nombres en español (`verbose_name`), representación `__str__` útil. |
| **API RESTful** | CRUD funcional. | ✅ **Filtros avanzados** (búsqueda, ordenamiento). Códigos HTTP precisos. URLs en español. |
| **Git / Versiones** | 5 commits progresivos. | ✅ **GitFlow / Conventional Commits** (en español: `feat/autenticacion`, `fix/bug`). |
| **Documentación** | README básico. | ✅ **README Profesional**: Badges, Setup Docker/Local, Diagrama ER. Docstrings en español. |

---

## REQUERIMIENTOS TÉCNICOS BASE (Traducidos)

### 1. Entidades del Sistema (ORM)
Todos los nombres de clases y atributos deben estar en **Español**.

**1. Empresa**
* `nombre`: CharField (indexado)
* `direccion`: TextField
* `rut`: CharField (con validación chilena)
* `creado_en`: DateTimeField (auto_now_add)

**2. Equipo**
* `empresa`: ForeignKey (Empresa)
* `nombre`: CharField
* `numero_serie`: CharField (Unique)
* `es_critico`: BooleanField (default=False)
* `fecha_instalacion`: DateField

**3. Tecnico** (Técnico)
* `usuario`: OneToOneField (User model de Django)
* `nombre_completo`: CharField
* `especialidad`: CharField (Choices: Eléctrico, Mecánico, Software, etc.)
* `telefono`: CharField

**4. PlanMantencion** (Plan de Mantención)
* `equipo`: ForeignKey (Equipo)
* `nombre`: CharField
* `frecuencia_dias`: IntegerField (Positive)
* `activo`: BooleanField (default=True)

**5. OrdenTrabajo** (Orden de Trabajo)
* `plan`: ForeignKey (PlanMantencion)
* `equipo`: ForeignKey (Equipo)
* `tecnico`: ForeignKey (Tecnico)
* `estado`: CharField (Choices: Programada, En Progreso, Completada, Cancelada)
* `fecha_programada`: DateTimeField
* `completado_en`: DateTimeField (null=True, blank=True)
* `notas`: TextField (blank=True)

### 2. Endpoints y Funcionalidad
Estructura de URL: `/api/v1/...` (Todo en español)

| Recurso | Rutas | Métodos | Permisos "Nivel 10" |
| :--- | :--- | :--- | :--- |
| **Auth** | `/auth/login/`, `/auth/refresh/` | POST | Público |
| **Empresas** | `/empresas/` | CRUD | Solo Admin o Auth |
| **Equipos** | `/equipos/` | CRUD | Auth (Lectura), Admin (Escritura) |
| **Técnicos** | `/tecnicos/` | CRUD | Solo Admin (Crear), Mismo Técnico (Editar perfil) |
| **Planes** | `/planes-mantencion/` | CRUD | Auth |
| **Órdenes** | `/ordenes-trabajo/` | CRUD | Técnico asignado cambia estado, Admin todo. |
| **Estado** | `/estado/` | GET | Público (Health Check) |

---

## INSTRUCCIONES FORMALES (Contexto)
*Fuente: TI3041 - Ev.4.pdf*

1. **Contexto:** Empresa de mantención industrial en Biobío.
2. **Entrega:** Repositorio GitHub.
3. **Puntaje Base:** 62 Puntos (Nosotros apuntamos a 100/100++).

**Regla de Oro:** Todo el código (variables, funciones, clases, comentarios, URLs) será en **ESPAÑOL**.
