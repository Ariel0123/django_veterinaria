from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Cliente(models.Model):
    nombre = models.CharField(max_length=250)
    primer_apellido = models.CharField(max_length=250)
    segundo_apellido = models.CharField(max_length=250)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=250)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.primer_apellido, self.segundo_apellido)

    @property
    def NombreCompleto(self):
        return '{} {} {}'.format(self.nombre, self.primer_apellido, self.segundo_apellido)

    def get_absolute_url(self):
        return reverse('cliente-id', kwargs={'pk': self.pk})


class Mascota(models.Model):

    SEX = (
        ('Hembra', 'Hembra'),
        ('Macho', 'Macho'),
        )

    dueno = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    foto = models.ImageField(default="default.png", upload_to='mascotas_pics')
    nombre = models.CharField(max_length=250)
    especie = models.CharField(max_length=250, blank=True)
    raza = models.CharField(max_length=250, blank=True)
    sexo = models.CharField(max_length=250, choices=SEX, default='Hembra')
    color = models.CharField(max_length=250, blank=True)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('mascota-id', kwargs={'pk': self.pk})


class Cita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    expediente = models.CharField(max_length=250)
    cita_fecha = models.DateField()
    vacunas = models.TextField()
    nota = models.TextField(blank=True)
    asistencia = models.BooleanField()

    def __str__(self):
        return '{} - Dueño: {}'.format(self.mascota.nombre, self.mascota.dueno.nombre)

    def get_absolute_url(self):
        return reverse('cita-id', kwargs={'pk': self.pk})


class RecetaSimple(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    expediente = models.CharField(max_length=250)
    receta = models.TextField()
    nota = models.TextField(blank=True)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.receta

    def get_absolute_url(self):
        return reverse('receta-id', kwargs={'pk': self.pk})


class Cirugia(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    expediente = models.CharField(max_length=250)
    causa = models.CharField(max_length=250)
    procedimiento = models.TextField()
    nota = models.TextField(blank=True)
    fecha_programada = models.DateField(blank=True)
    realizada = models.BooleanField()
    fecha = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.procedimiento

    def get_absolute_url(self):
        return reverse('cirugia-id', kwargs={'pk': self.pk})

class RecetaCirugia(models.Model):
    cirugia = models.ForeignKey(Cirugia, on_delete=models.CASCADE)
    expediente = models.CharField(max_length=250)
    receta = models.TextField()
    nota = models.TextField(blank=True)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.receta

    def get_absolute_url(self):
        return reverse('recetacirugia-id', kwargs={'pk': self.pk})






