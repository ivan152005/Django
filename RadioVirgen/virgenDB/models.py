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
class Pago_con_tarjeta(models.Model):
    numero_tarjeta = models.IntegerField()
    cvc = models.IntegerField(default=3)
    nombre_completo = models.CharField(max_length=40)
    predeterminado = models.BooleanField(default=False)

class Paypal(models.Model):
    correo_electronico = models.CharField(max_length=40)
    predeterminado = models.BooleanField(default=True)

class Transferencia_bancaria(models.Model):
    numero_cuenta = models.CharField(max_length=20)
    nombre_cuenta = models.CharField(max_length=100)
    predeterminado = models.BooleanField(default=False)

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
class Metodos_pago(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    pago_con_tarjeta = models.ForeignKey(Pago_con_tarjeta, on_delete=models.CASCADE, null=True)
    paypal = models.ForeignKey(Paypal, on_delete=models.CASCADE, null=True)
    transferencia_bancaria = models.ForeignKey(Transferencia_bancaria, on_delete=models.CASCADE, null=True)

class Reproducciones(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idPodcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    numReproducciones = models.IntegerField()
    def __str__(self):
        return f'Usuario: {self.idUsuario.__str__()} - Podcast: {self.idPodcast} - Reproducciones: {self.numReproducciones}'



