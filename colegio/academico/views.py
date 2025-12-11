from django.shortcuts import render
from academico.models import Alumno, Nota

#ANTES USAR EL INSERTAR DATOS
#py manage.py makemigrations
#py manage.py migrate
#py manage.py insertar_datos
#py manage.py runserver

def mostrarIndex(request):
    return render(request,'index.html')
#---------------------------------------------------------------------
#-----------------------Registrar Notas--------------------------------
#---------------------------------------------------------------------
def MostrarFormRegistrarNotas(request):
    alu = Alumno.objects.all().values().order_by("nombre")
    datos ={ 'alu':alu}
    return render(request, 'form_registrar_notas.html' ,datos)

def InsertarNotas(request):
    if request.method == 'POST':
        alu= request.POST['cboalu']
        mat= request.POST['cbomat']
        nota= request.POST['txtnot']

        alumno = Alumno.objects.get(id=alu)

        notaa = float(nota)
        if notaa <1 or notaa >7:
            datos = {'r2':'Nota debe ser entre 1.0 y 7.0'}
            return render(request,  'form_registrar_notas.html', datos)

        notas = Nota(alumno=alumno, materia=mat, nota=notaa)
        notas.save()
        datos = {'r':'Nota ingresada correctamente'}
        return render(request,  'form_registrar_notas.html', datos)
    else:
        datos = {'notas':notas, 'r2':'Error al ingresar la Nota'}
        return render(request,  'form_registrar_notas.html', datos)
#---------------------------------------------------------------------
#-----------------------Modificar Notas--------------------------------
#---------------------------------------------------------------------
def MostrarModificarNotas(request,id):
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
        'materias': materias  
    }
    return render(request, 'form_actualizar.html', datos)

def ModificarNotas(request,id):
    if request.method == 'POST':
        alu = request.POST['cboalu']
        mat = request.POST['cbomat']
        nota = request.POST['txtnot']

        notas = Nota.objects.get(id = id)

        notas.alumno = Alumno.objects.get(id= alu) 
        notas.materia = mat
        notas.nota = float(nota)
        notas.save()
        notas = Nota.objects.select_related("alumno").all()

        datos = {'r': 'La nota ha sido modificada exitosamente', 'nota': nota , 'notas':notas}
        return render(request, 'listado_notas.html', datos)
    else:
            return render(request, 'form_actualizar.html')
#---------------------------------------------------------------------
#-----------------------Eliminar Notas--------------------------------
#---------------------------------------------------------------------
def EliminarNotas(request,id):
    try:
        nota = Nota.objects.get(id = id)
        nom = nota.alumno.nombre 
        nota.delete()
        notas = Nota.objects.select_related("alumno").all()
        datos = {'nom' :nom,'r':'La nota fue eliminada ('+str(nom.upper())+') ','notas':notas}
        return render(request,  'listado_notas.html',datos)
    except:
        notas = Nota.objects.select_related("alumno").all()
        datos = {'nom' :nom,'r':'La nota no existe ('+str(id)+')','notas':notas}
        return render(request,  'listado_notas.html',datos)


#---------------------------------------------------------------------
#-----------------------Listar Notas--------------------------------
#---------------------------------------------------------------------
def MostrarListadoNotas(request):
    notas = Nota.objects.select_related("alumno").all()
    datos= {'notas' :notas}
    return render(request,  'listado_notas.html', datos)
#---------------------------------------------------------------------
#-----------------------Listar Alumnos --------------------------------
#---------------------------------------------------------------------
def MostrarListadoAlumnos(request):
    alu = Alumno.objects.all()
    datos= {'alu' :alu}
    return render(request,  'listado_alumnos.html', datos)

#---------------------------------------------------------------------
#-----------------------eliminar Alumnos --------------------------------
#---------------------------------------------------------------------

def EliminarAlumnos(request,id):
    alu = Alumno.objects.get(id=id)
    nom = alu.nombre
    alu.delete()
    alu = Alumno.objects.all()
    datos= {'alu' :alu,'r':'El Alumno/a fue eliminado/a ('+str(nom.upper())+')'}
    return render(request,  'listado_alumnos.html', datos)

#---------------------------------------------------------------------
#-----------------------Actualizar Alumnos --------------------------------
#---------------------------------------------------------------------
def MostrarModificarAlumnos(request,id):
    alu = Alumno.objects.get(id=id)
    datos= {'alu' :alu}
    return render(request,'form_actualizar_alumnos.html',datos)

def ModificarAlumnos(request,id):
    nom = request.POST['txtnom']
    cur = request.POST['txtcur']
    mat = request.POST['txtmat']
    
    alu = Alumno.objects.get(id=id)
    alu.nombre = nom
    alu.curso = cur
    alu.matricula = mat
    alu.save()

    alu = Alumno.objects.all()
    datos= {'r': 'Alumno/a ha sido modificado/a exitosamente','alu' :alu}
    return render(request,'listado_alumnos.html',datos)

#---------------------------------------------------------------------
#-----------------------registrar Alumnos --------------------------------
#---------------------------------------------------------------------
def MostrarFormRegistrarAlumnos(request):
    return render(request,'form_registrar_alumnos.html')

def InsertarAlumnos(request):
    nom = request.POST['txtnom']
    cur = request.POST['txtcur']
    mat = request.POST['txtmat']

    alu = Alumno(nombre=nom, curso=cur, matricula=mat)
    alu.save()
    datos = {'r':'Nota ingresada correctamente','alu':alu}
    return render(request,'form_registrar_alumnos.html',datos)

