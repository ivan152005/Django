import datetime

from django.db import models

# Create your models here.
class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    numMaxAutores = models.IntegerField(default=5)

    def __str__(self):
        return f'ID: {self.id.__str__()} - {self.nombre}'

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f'ID: {self.id.__str__()} - {self.nombre}'


class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(decimal_places=2, max_digits=5)
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(nombre__in=['Individual', 'Jubilado', 'Estudiante', 'Familiar']),  name="ch_plan_nombre")
        ]
    def __str__(self):
        return f'ID: {self.id.__str__()} - {self.nombre}'


class Podcast(models.Model):
    nombre = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor, blank=False)
    categoria = models.CharField(max_length=100)
    fecha_baja = models.DateField(null=True, blank=True)
    likes = models.IntegerField()
    numReproducciones = models.IntegerField()
    urlDrive = models.CharField(max_length=200)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(categoria__in=['Educativo', 'Comedia', 'Formacion']),   name="ch_categoria")
        ]

    def __str__(self):
        return f'ID: {self.id.__str__()} - {self.nombre}'

class Familia(models.Model):
    nombre = models.CharField(max_length=100)
    max_miembros = models.IntegerField(default=4)
    def __str__(self):
        return f'ID: {self.id.__str__()} - {self.nombre}'

class Usuario(models.Model):
    nick = models.CharField(unique=True, max_length=100)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    fecha_de_alta = models.DateField()
    fecha_de_baja = models.DateField(null=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, null=True, blank=True)
    podcast_pendientes = models.ManyToManyField(Podcast, related_name="fk_user_podcast_pend", blank=True)
    me_gusta_podcast = models.ManyToManyField(Podcast, related_name="fk_user_podcast_liked", blank=True)
    def __str__(self):
        return f'ID: {self.id.__str__()} - {self.nombre}'

class Reproducciones(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idPodcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    numReproducciones = models.IntegerField()
    def __str__(self):
        return f'Usuario: {self.idUsuario.__str__()} - Podcast: {self.idPodcast} - Reproducciones: {self.numReproducciones}'



