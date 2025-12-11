from django.core.management.base import BaseCommand
from academico.models import Alumno,Nota, Usuarios;


class Command(BaseCommand):
        help = 'Inserta Estado,Usuarios,Tematica,Foro y Comentario en la base de datos'

        def handle(self, *args, **kwargs):
                usu = [
                Usuarios(nombre= 'Maria Carmen Pinto', 
                rut='11222333-4',
                contraseña= '123'),
                Usuarios(nombre= 'Mario Soto Perez', 
                rut='44333222-1',
                contraseña= '321'
                ),
                Usuarios(nombre= 'Sofía Martínez González', 
                rut='33333333-3',
                contraseña= '333'
                ),
                Usuarios(nombre= 'Pablo Rodríguez López', 
                rut='44444444-4',
                contraseña= '444'
                ),
                Usuarios(nombre= 'Lucía Fernández Castro', 
                rut='55555555-5',
                contraseña= '555'
                ),
                ]
                Usuarios.objects.bulk_create(usu)
                self.stdout.write(self.style.SUCCESS('Usuarios creadas exitosamente.'))

                
                alumno = [
                Alumno(nombre= 'Daniel Javier Gutierrez de la Cruz',
                        curso='2°A',
                        matricula='A2022-023',
                        apoderado = Usuarios.objects.get(id=2)), 
                Alumno(nombre='Maria Jasmin Sandoval Fuentes' ,
                        curso= '1°B',
                        matricula='B2023-045',
                        apoderado = Usuarios.objects.get(id=3)), 
                Alumno(nombre='Rodrigo Miguel Cancino Mendoza ' ,
                        curso='3°A',
                        matricula='A2023-001',
                        apoderado = Usuarios.objects.get(id=4)),
                Alumno(nombre='Sofia Zoe Inostroza Alvarez ' ,
                        curso='4°A',
                        matricula='A2023-003',
                        apoderado = Usuarios.objects.get(id=5)), 
                ]
                Alumno.objects.bulk_create(alumno)
                self.stdout.write(self.style.SUCCESS('Alumnos creados exitosamente.'))

                nota = [
                Nota(alumno = Alumno.objects.get(id=1), 
                materia='Ciencias Naturales',
                nota= 5.0),
                Nota(alumno = Alumno.objects.get(id=1), 
                materia='Ciencias Naturales',
                nota= 3.0),
                Nota(alumno = Alumno.objects.get(id=2), 
                materia='Historia, Geografía y Ciencias Sociales',
                nota= 4.0),
                Nota(alumno = Alumno.objects.get(id=3), 
                materia='Educación Física',
                nota= 6.0),
                Nota(alumno = Alumno.objects.get(id=4), 
                materia='Tecnología',
                nota= 7.0),
                ]
                Nota.objects.bulk_create(nota)
                self.stdout.write(self.style.SUCCESS('Nota creadas exitosamente.'))
                
                
                
        


