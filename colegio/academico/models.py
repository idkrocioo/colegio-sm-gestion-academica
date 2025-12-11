from django.db import models

class Alumno(models.Model):
    nombre = models.TextField(max_length=100)
    curso = models.TextField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)

class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.TextField(max_length=100)
    nota = models.FloatField()

class Promedio(models.Model):
    alumno_prom = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    promedio= models.FloatField()
    materia = models.TextField(max_length=100)