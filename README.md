# 🏫 Sistema de Gestión Académica – Colegio San Martín de Oasis  
Plataforma web desarrollada con **Django** para la administración de notas, alumnos y módulos académicos.  
Interfaz moderna, funcional y adaptada a procesos reales del establecimiento.

---

## ✨ Descripción General

Este sistema permite gestionar de forma eficiente la información académica del Colegio San Martín de Oasis.  
Incluye herramientas para:

- ✔ Registro y actualización de notas  
- ✔ Control estudiantil (inscripción, edición y consulta de alumnos)  
- ✔ Autenticación y sesiones por usuario  
- ✔ Menús dinámicos según permisos  
- ✔ Diseño moderno con gradientes e identidad visual institucional  

Es un proyecto real utilizado como apoyo para la administración interna del colegio.

---

## 🚀 Tecnologías Utilizadas

### **Backend**
- Python 3  
- Django 4  

### **Frontend**
- HTML5  
- CSS3  
- Bootstrap  
- Templates Django (Jinja)

### **Base de datos**
- SQLite (por defecto, configurable a PostgreSQL)

### **Otros**
- Git / GitHub  
- Entorno Windows / Linux  

---

## 📸 Capturas del Sistema

> 📌 Coloca tus imágenes en una carpeta llamada **/docs** dentro del repositorio  
> Ejemplo: `docs/login.png`, `docs/dashboard.png`

### **🔐 Login**
![Login](docs/login.png)

### **🏠 Dashboard Principal**
![Dashboard](docs/dashboard.png)

### **📝 Formulario de Notas**
![Formulario Notas](docs/form_notas.png)

### **👨‍🎓 Listado de Alumnos**
![Listado Alumnos](docs/listado_alumnos.png)

---

## ▶ Instalación y Ejecución del Proyecto

### **1. Clonar repositorio**
git clone https://github.com/idkrocioo/colegio-sm-gestion-academica.git
cd colegio-sm-gestion-academica

### **2. Crear entorno virtual**
python -m venv venv

### **3. Activar entorno**
Windows:
venv\Scripts\activate

### **4. Instalar dependencias**
pip install django

### **5. Aplicar migraciones**
python manage.py migrate

### **6. Ejecutar servidor**
python manage.py runserver

El sistema estará disponible en:  
👉 http://127.0.0.1:8000/

---

## 📌 Funcionalidades del Sistema

### 🔐 Autenticación
- Login de usuarios  
- Manejo de sesiones  

### 📝 Gestión Académica
- Registro de notas  
- Listado de notas  
- Edición de notas  

### 🧑‍🎓 Control Estudiantil
- Registro de alumnos  
- Edición de información  
- Listado dinámico con filtros  

### 🎨 Diseño
- Gradientes personalizados  
- Interfaz responsiva  
- Componentes reutilizables  

---

## 📌 Próximas mejoras
- Implementación de roles (Admin / Profesor)  
- Exportación de notas a PDF o Excel  
- Integración con API REST  
- Dashboard estadístico  

---

## 👩‍💻 Autora

**Rocío Belén Orellana Díaz**  
Estudiante de Ingeniería en Informática – INACAP  
📧 rocio.orellana.ing@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/rocío-orellana-díaz-3854b7269  

---

## ⭐ Agradecimientos
Proyecto desarrollado como parte de estudios y colaboración con el Colegio San Martín de Oasis.


## 📁 Estructura del Proyecto

```text
colegio-sm-gestion-academica/
├─ academico/
│  ├─ management/
│  ├─ migrations/
│  ├─ static/
│  ├─ templates/
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
├─ colegio/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ INSTRUCCIONES.txt
└─ manage.py
