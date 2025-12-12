from django.shortcuts import render
from academico.models import Alumno, Nota, Usuarios
from django.contrib import messages
from django.utils import timezone

#ANTES USAR EL INSERTAR DATOS
#py manage.py makemigrations
#py manage.py migrate
#py manage.py insertar_datos
#py manage.py runserver

def mostrarIndex(request):
    return render(request,'index.html')

def IniciarSesion(request):
    if request.method == "POST":
        rut = request.POST.get("txtusu")
        pas = request.POST.get("txtpas")
        
        try:
            usuario = Usuarios.objects.get(rut=rut)
            
            if usuario.contraseña == pas:
                request.session["estadoSesion"] = True
                request.session["idUsuario"] = usuario.id
                request.session["nomUsuario"] = usuario.nombre
                request.session["rutUsuario"] = usuario.rut
                
                # Datos para el dashboard
                datos = {
                    "nomUsuario": usuario.nombre, 
                    "rutUsuario": usuario.rut, 
                    "idUsuario": usuario.id
                }
                
                # Usar dashboard.html para ambos tipos de usuarios
                return render(request, 'dashboard.html', datos)
                
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
                return render(request, 'index.html')
                
        except Usuarios.DoesNotExist:
            messages.error(request, "Acceso denegado. Usuario o contraseña incorrectos.")
            return render(request, 'index.html')
    else:
        messages.error(request, "No se puede procesar la solicitud.")
        return render(request, 'index.html')

def CerrarSesion(request):
    try:
        del request.session["estadoSesion"]
        del request.session["idUsuario"]
        del request.session["rutUsuario"]
        del request.session["nomUsuario"]
        datos = { 'r': 'Sesión cerrada correctamente'}
        return render(request,'index.html',datos)
    
    except:
        datos = {'r2': 'No se puede procesar la solicitud.'}
        return render(request,'index.html',datos)
    
def volverMenu(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        rutUsuario = request.session.get("rutUsuario")
        if rutUsuario == "11222333-4":
            nomUsuario = request.session.get("nomUsuario")
            datos = {
                "nomUsuario": nomUsuario,
                "rutUsuario": rutUsuario
            }
            return render(request, 'dashboard.html', datos)
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html', datos)
    else:
        datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
        return render(request, 'index.html', datos)

#---------------------------------------------------------------------
#-----------------------Registrar Notas--------------------------------
#---------------------------------------------------------------------
def MostrarFormRegistrarNotas(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        rutUsuario = request.session.get("rutUsuario")
        if rutUsuario == "11222333-4":
            nomUsuario = request.session.get("nomUsuario")
            alu = Alumno.objects.all().values().order_by("nombre")
            datos ={ 'alu':alu, 'nomUsuario': nomUsuario}
            return render(request, 'registro_notas.html', datos)
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html', datos)
    else:
        datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
        return render(request, 'index.html', datos)

def InsertarNotas(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")
    rutUsuario = request.session.get("rutUsuario")
    if estadoSesion is True:
        if rutUsuario == "11222333-4":
            if request.method == 'POST':
                alu= request.POST['cboalu']
                mat= request.POST['cbomat']
                nota= request.POST['txtnot']

                alumno = Alumno.objects.get(id=alu)

                notaa = float(nota)
                if notaa <1 or notaa >7:
                    datos = {'r2':'Nota debe ser entre 1.0 y 7.0'}
                    return render(request,  'registro_notas.html', datos)

                notas = Nota(alumno=alumno, materia=mat, nota=notaa)
                notas.save()
                datos = {'r':'Nota ingresada correctamente'}
                return render(request,  'registro_notas.html', datos)
            else:
                datos = {'r2':'Error al ingresar la Nota'}
                return render(request,  'registro_notas.html', datos)
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html',datos)
    else:
        datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
        return render(request, 'index.html',datos)
    
#---------------------------------------------------------------------
#-----------------------Modificar Notas--------------------------------
#---------------------------------------------------------------------
def MostrarModificarNotas(request, id):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        rutUsuario = request.session.get("rutUsuario")
        if rutUsuario == "11222333-4":
            nomUsuario = request.session.get("nomUsuario")
            nota = Nota.objects.select_related('alumno').get(id=id)
            
            alumnos = Alumno.objects.all().order_by("nombre")
            materias = [
                "Lengua y Literatura",
                "Matemática",
                "Ciencias Naturales",
                "Historia, Geografía y Ciencias Sociales",
                "Arte",
                "Educación Física",
                "Religión",
                "Tecnología",
                "Inglés",
                "Educación para la Ciudadanía",
                "Música"
            ]

            datos = {
                'nota': nota,         
                'alumnos': alumnos,   
                'materias': materias,
                'nomUsuario': nomUsuario
            }
            return render(request, 'actualizar_notas.html', datos)
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html', datos)
    else:
        datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
        return render(request, 'index.html', datos)
    
def ModificarNotas(request, id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:
            rutUsuario = request.session.get("rutUsuario")
            if rutUsuario == "11222333-4":
                nomUsuario = request.session.get("nomUsuario")
                if request.method == 'POST':
                    alu = request.POST['cboalu']
                    mat = request.POST['cbomat']
                    nota_valor = request.POST['txtnot']

                    nota = Nota.objects.get(id = id)
                    nota.alumno = Alumno.objects.get(id= alu) 
                    nota.materia = mat
                    nota.nota = float(nota_valor)
                    nota.save()
                    
                    notas = Nota.objects.select_related("alumno").all()
                    
                    datos = {
                        'r': 'La nota ha sido modificada exitosamente', 
                        'notas': notas,
                        'nomUsuario': nomUsuario
                    }
                    return render(request, 'listado_notas.html', datos)
                else:
                    # Si no es POST, redirigir al formulario de modificación
                    return MostrarModificarNotas(request, id)
            else:
                datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
                return render(request, 'index.html', datos)
        else:
            datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
            return render(request, 'index.html', datos)
    except Exception as e:
        datos = {'r2': 'No se pudo modificar la nota!!'}
        return render(request, 'actualizar_notas.html', datos)

#---------------------------------------------------------------------
#-----------------------Eliminar Notas--------------------------------
#---------------------------------------------------------------------
def EliminarNotas(request,id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:
            rutUsuario = request.session.get("rutUsuario")
            if rutUsuario == "11222333-4":
                nomUsuario = request.session.get("nomUsuario")
                nota = Nota.objects.get(id = id)
                nom = nota.alumno.nombre 
                nota.delete()
                notas = Nota.objects.select_related("alumno").all()
                datos = {'nom' :nom,'r':'La nota fue eliminada ('+str(nom.upper())+') ','notas':notas}
                return render(request,  'listado_notas.html',datos)
            else:
                datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
                return render(request, 'index.html',datos)
        else:
            datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
            return render(request, 'index.html',datos)
    except Exception as e:
        notas = Nota.objects.select_related("alumno").all()
        datos = {'r':'La nota no existe ('+str(id)+')','notas':notas}
        return render(request,  'listado_notas.html',datos)

#---------------------------------------------------------------------
#-----------------------Listar Notas--------------------------------
#---------------------------------------------------------------------
def MostrarListadoNotas(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        rutUsuario = request.session.get("rutUsuario")
        if rutUsuario == "11222333-4":
            nomUsuario = request.session.get("nomUsuario")
            notas = Nota.objects.select_related("alumno").all()
            datos = {
                'notas': notas,
                'nomUsuario': nomUsuario
            }
            return render(request, 'listado_notas.html', datos)
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html', datos)
    else:
        datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
        return render(request, 'index.html', datos)

#---------------------------------------------------------------------
#-----------------------Listar Alumnos --------------------------------
#---------------------------------------------------------------------
def MostrarListadoAlumnos(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        rutUsuario = request.session.get("rutUsuario")
        if rutUsuario == "11222333-4":
            nomUsuario = request.session.get("nomUsuario")
            alu = Alumno.objects.all()
            datos = {
                'alu': alu,
                'nomUsuario': nomUsuario
            }
            return render(request, 'listado_alumnos.html', datos)
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html', datos)
    else:
        datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
        return render(request, 'index.html', datos)

#---------------------------------------------------------------------
#-----------------------eliminar Alumnos --------------------------------
#---------------------------------------------------------------------
def EliminarAlumnos(request,id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:
            rutUsuario = request.session.get("rutUsuario")
            if rutUsuario == "11222333-4":
                nomUsuario = request.session.get("nomUsuario")
                alu = Alumno.objects.get(id=id)
                nom = alu.nombre
                alu.delete()
                alu = Alumno.objects.all()
                datos= {'alu' :alu,'r':'El Alumno/a fue eliminado/a ('+str(nom.upper())+')'}
                return render(request,  'listado_alumnos.html', datos)
            else:
                datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
                return render(request, 'index.html',datos)
        else:
            datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
            return render(request, 'index.html',datos) 
    except Exception as e:
        alu = Alumno.objects.all()
        datos = {'r2': 'Error al eliminar el Alumno/a!!', 'alu':alu}
        return render(request,  'listado_alumnos.html', datos)

#---------------------------------------------------------------------
#-----------------------Actualizar Alumnos --------------------------------
#---------------------------------------------------------------------
def MostrarModificarAlumnos(request, id):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        rutUsuario = request.session.get("rutUsuario")
        if rutUsuario == "11222333-4":
            nomUsuario = request.session.get("nomUsuario")
            alu = Alumno.objects.get(id=id)
            datos = {
                'alu': alu,
                'nomUsuario': nomUsuario  # Para mantener consistencia
            }
            return render(request, 'form_actualizar_alumnos.html', datos)
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html', datos)
    else:
        datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
        return render(request, 'index.html', datos)

def ModificarAlumnos(request,id):
    try:
        estadoSesion = request.session.get("estadoSesion")
        if estadoSesion is True:
            rutUsuario = request.session.get("rutUsuario")
            if rutUsuario == "11222333-4":
                nomUsuario = request.session.get("nomUsuario")
                nom = request.POST['txtnom']
                cur = request.POST['txtcur']
                mat = request.POST['txtmat']
                rut = request.POST['txtrut']
                apo_nombre = request.POST['txtapo']
                pas = request.POST['txtpas']
                
                alu = Alumno.objects.get(id=id)
                alu.nombre = nom
                alu.curso = cur
                alu.matricula = mat

                apo = alu.apoderado 
                apo.rut = rut
                apo.nombre = apo_nombre
                apo.contraseña = pas
                apo.save()

                alu.save()

                alu = Alumno.objects.all()
                datos= {'r': 'Alumno/a ha sido modificado/a exitosamente','alu' :alu}
                return render(request,'listado_alumnos.html',datos)
            else:
                datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
                return render(request, 'index.html',datos)
        else:
            datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
            return render(request, 'index.html',datos)
    except Exception as e:
        alu = Alumno.objects.all()
        datos = {'r':'El alumno no existe ('+str(id)+') o ocurrio un error inesperado','alu':alu}
        return render(request,  'listado_alumnos.html',datos)
        
#---------------------------------------------------------------------
#-----------------------registrar Alumnos --------------------------------
#---------------------------------------------------------------------
def MostrarFormRegistrarAlumnos(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        rutUsuario = request.session.get("rutUsuario")
        if rutUsuario == "11222333-4":
            nomUsuario = request.session.get("nomUsuario")
            return render(request, 'form_registrar_alumnos.html', {'nomUsuario': nomUsuario})
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html', datos)
    else:
        datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
        return render(request, 'index.html', datos)

def InsertarAlumnos(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        rutUsuario = request.session.get("rutUsuario")
        if rutUsuario == "11222333-4":
            nomUsuario = request.session.get("nomUsuario")
            nom = request.POST['txtnom']
            cur = request.POST['txtcur']
            mat = request.POST['txtmat']
            rut = request.POST['txtrut']
            apo = request.POST['txtapo']
            pas = request.POST['txtpas']
            apo = Usuarios(rut=rut,nombre=apo, contraseña=pas)
            apo.save()

            alu = Alumno(nombre=nom, curso=cur, matricula=mat, apoderado = apo)
            alu.save()
            datos = {'r': 'Alumno registrado correctamente', 'nomUsuario': nomUsuario}
            return render(request, 'registro_alumno.html', datos)
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html', datos)
    else:
        datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
        return render(request, 'index.html', datos)
    
#-------------------------APODERADOS------------------------------------
def MostrarListadoNotasAlumno(request,id):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        rutUsuario = request.session.get("rutUsuario")
        if rutUsuario != "11222333-4":
            idUsuario = request.session.get("idUsuario")
            alu = Alumno.objects.get(apoderado = idUsuario)
            notas = Nota.objects.select_related("alumno").filter(alumno=alu).order_by("materia")
            datos = {'notas':notas}
            return render(request,'listado_notas_alumno.html',datos)
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html',datos)
    else:
        datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
        return render(request,'index.html',datos)
    
def volverMenu2(request):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        rutUsuario = request.session.get("rutUsuario")
        idUsuario = request.session.get("idUsuario")
        if rutUsuario != "11222333-4":
            nomUsuario = request.session.get("nomUsuario")
            datos = {
                "nomUsuario": nomUsuario,
                "rutUsuario": rutUsuario,
                "idUsuario": idUsuario
            }
            return render(request, 'dashboard.html', datos)
        else:
            datos = {'r2': 'No tiene permisos suficientes para acceder!!'}
            return render(request, 'index.html', datos)
    else:
        datos = {'r2': 'Debe iniciar sesion para acceder!!!'}
        return render(request, 'index.html', datos)