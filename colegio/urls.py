
from django.contrib import admin
from django.urls import path
from academico import views

urlpatterns = [
    path('admin/', admin.site.urls),

#-----------------------------INDEX -------------------------
    path('',views.mostrarIndex),

#-----------------------------INICIO DE USUARIO -------------------------
    path('login',views.IniciarSesion),

#-----------------------------CIERRA SESION -------------------------
    path('logout/',views.CerrarSesion),


#------------------------------BOTON DE REGRESAR AL MENU PRINCIPAL----------------------
path('menu_principal',views.volverMenu),

#-----------------------------REGISTRAR NOTAS-------------------------
    path('form_registrar_notas',views.MostrarFormRegistrarNotas),
    path('form_registrar_nota',views.InsertarNotas),
    
#-----------------------------LISTAR NOTAS-------------------------
    path('listado_notas',views.MostrarListadoNotas),

#-----------------------------MODIFICAR NOTAS-------------------------
    path('form_actualizar_notas/<int:id>',views.MostrarModificarNotas),
    path('actualizar_notas/<int:id>',views.ModificarNotas),
#-----------------------------ELIMINAR NOTAS-------------------------
    path('eliminar_nota/<int:id>',views.EliminarNotas),

#-----------------------------LISTAR ALUMNOS-------------------------
    path('listado_alumnos',views.MostrarListadoAlumnos),
#-----------------------------MODIFICAR ALUMNOS-------------------------
    path('form_actualizar_alumno/<int:id>',views.MostrarModificarAlumnos),
    path('actualizar_alumnos/<int:id>',views.ModificarAlumnos),
#-----------------------------ELIMINAR ALUMNOS-------------------------
    path('eliminar_alumno/<int:id>',views.EliminarAlumnos),
#-----------------------------REGISTRAR ALUMNOS-------------------------
    path('form_registrar_alumnos',views.MostrarFormRegistrarAlumnos),
    path('form_registrar_alumno',views.InsertarAlumnos),

#---------------------------------APODERADO CON UN ALUMNO---------------------------

    path('listado_notas_alumno/<int:id>', views.MostrarListadoNotasAlumno),

#------------------------------BOTON DE REGRESAR AL MENU PRINCIPAL----------------------
    path('menu_principal2', views.volverMenu2 )
]

