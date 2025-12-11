# Referencia del Proyecto - Evaluación 4 (Backend)

## Instrucciones del Proyecto (TI3041 - Ev.4)

### Presentación
**Unidad de Aprendizaje 3:** API restful con integración a base de datos.
**Aprendizaje esperado:** 3.1 Codifica una API restful con el fin de conectarse con otras aplicaciones, utilizando autenticación JWT.

**Criterios de evaluación:**
* 3.1.1 Configura Django Rest framework, según la documentación oficial.
* 3.1.2 Codifica instrucciones de autenticación, de acuerdo a los requerimientos.
* 3.1.3 Codifica instrucciones que generen resultados en formato JSON, de acuerdo con los requerimientos.
* 3.1.4 Codifica una API funcional, que sea restful.

**Actividades:**
1. Desarrollar una aplicación API RestFul. Utilizando el framework DjangoRest.

### Instrucciones
1. Revisar el instrumento de evaluación sumativa.
2. Elabora la aplicación web respondiendo a los requerimientos entregados.
3. Entregar el proyecto por GitHub, compartiendo la URL en un bloc de notas adjuntando a la plataforma de INACAP.

### Requerimientos del Proyecto
**Contexto:** Desarrollar una API RESTful para una empresa de mantención industrial de la Región del Biobío, destinada a registrar empresas clientes, equipos, técnicos, planes de mantención y órdenes de trabajo.

#### 1. Configuración del Framework
* Configurar correctamente Django REST Framework en el proyecto.
* Habilitar la API navegable.
* Definir JSON como formato de respuesta estándar.
* Configurar permisos base de acceso para la API.
* Habilitar un mecanismo de autenticación de usuarios.

#### 2. ORM (Entidades y Atributos)
Se deben implementar, como mínimo, las siguientes entidades y atributos:

1. **Empresa**
   * name
   * address
   * rut
   * created_at

2. **Equipo**
   * company
   * name
   * serial_number
   * critical
   * installed_at

3. **Técnico**
   * user
   * full_name
   * specialty
   * phone

4. **Plan de Mantención**
   * equipment
   * name
   * frequency_days
   * active

5. **Orden de Trabajo**
   * plan
   * equipment
   * technician
   * status
   * scheduled_date
   * completed_at
   * notes

#### 3. Serialización y formato de respuesta
* Implementar mecanismos de serialización para cada entidad.
* Todas las respuestas de la API deben entregarse en formato JSON.
* Incluir al menos un endpoint de prueba que permita validar el correcto funcionamiento general de la API.

#### 4. Desarrollo de la API RESTful
Para cada una de las cinco entidades, la API debe permitir:
* Crear registros (POST)
* Consultar registros (GET)
* Modificar registros (PUT/PATCH)
* Eliminar registros (DELETE)

**Endpoints:**
* Estar organizados por recurso (por ejemplo: /api/companies/, /api/equipments/, etc.).
* Usar correctamente los métodos HTTP según la operación.
* Entregar respuestas en JSON coherentes con la acción realizada.

#### 5. Autenticación y control de acceso
* Implementar un sistema de autenticación de usuarios.
* **Reglas de acceso:**
  * Usuarios no autenticados: solo pueden consultar información (lectura).
  * Usuarios autenticados: pueden crear, modificar y eliminar registros.

#### 6. Documentación
* Comentarios o docstrings en partes relevantes del código.
* **README** con:
  * Descripción breve del proyecto.
  * Requisitos (dependencias).
  * Pasos para ejecutar la API (migraciones, creación de usuario, runserver).
  * Ejemplos de endpoints.

### Forma de entrega
Repositorio Git con al menos 5 commits progresivos (base, modelos, serializers/vistas, autenticación, ajustes finales).

---

## Escala de Evaluación (Rúbrica)

### Criterios y Puntajes

| Criterios de evaluación | Indicadores | Escala de valoración | Puntaje |
| --- | --- | --- | --- |
| | | Excelente (5/6/8) | Bueno | Insatisfactorio | Deficiente (0) |
| **3.1.1 Configuración DRF** | Instala e Integra DRF en el proyecto. | 5 | 3 | 2 | 0 |
| **3.1.1 Configuración global** | Configura el REST_FRAMEWORK (JSON renderers, API navegable, permisos y autenticación). | 5 | 3 | 2 | 0 |
| **3.1.2 Autenticación** | Implementa un sistema de autenticación (sesión, token u otro método válido). | 6 | 4 | 2 | 0 |
| **3.1.2 Control de acceso** | Implementa una restricción que solo usuarios autenticados pueden crear, modificar o eliminar registros. | 6 | 4 | 2 | 0 |
| **3.1.3 Serialización JSON** | Usa serializers y retorna respuestas JSON en los endpoints. | 5 | 3 | 2 | 0 |
| **3.1.3 Endpoint de estado** | Valida la disponibilidad general de la API mediante un endpoint, entregando datos en JSON. | 3 | 2 | 1 | 0 |
| **3.1.4 Modelado de entidades** | Implementa correctamente 5 entidades con relaciones coherentes. | 8 | 5 | 3 | 0 |
| **3.1.4 API RESTful completa** | Implementa endpoints funcionales (CRUD) para todas las entidades usando métodos HTTP correctos. | 8 | 5 | 3 | 0 |
| **Control de versiones (Git)** | Evidencia un repositorio con mínimo 5 commits progresivos. | 6 | 4 | 2 | 0 |
| **Documentación del proyecto** | Documenta un README claro y documentación básica del código. | 5 | 3 | 2 | 0 |
| **Buenas prácticas de código** | Escribe un código organizado, nombres descriptivos, mantiene modularidad y legibilidad. | 5 | 3 | 2 | 0 |
