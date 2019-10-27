from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TipoUsuario(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, null = False,blank = False)
    descripcion = models.CharField(max_length = 110, blank = False, null = False)
    activo = models.BooleanField(default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Tipo Usuario'
        verbose_name_plural = 'Tipos de Usuario'

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    # id = models.AutoField(primary_key = True)
    # nombre = models.CharField(max_length = 100, null = False,blank = False)
    # password = models.CharField(max_length = 100, null = False,blank = False)
    # correo = models.EmailField(blank = False, null = False)
    # activo = models.BooleanField(default = True)
    # creado = models.DateField(auto_now = False,auto_now_add = True)

    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.DO_NOTHING, null=False, default=3)
    foto_perfil = models.URLField(max_length = 255, blank = False, null= False, default="https://www.info-computer.com/blog/wp-content/uploads/2018/04/fotoinicio.jpg")

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class TipoHabitacion(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, null = False,blank = False)
    descripcion = models.CharField(max_length = 110, blank = False, null = False)
    activo = models.BooleanField( default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Tipo Habitacion'
        verbose_name_plural = 'Tipos de Habitacion'

    def __str__(self):
        return self.nombre

class Habitacion(models.Model):
    id = models.AutoField(primary_key = True)
    tipoHabitacion =  models.ForeignKey(TipoHabitacion,on_delete=models.DO_NOTHING, null=False)
    numero = models.IntegerField(blank=True, null=True)
    piso = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length = 110, blank = False, null = False)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    activo = models.BooleanField( default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'

    def __str__(self):
        return self.numero

class ImagenHabitacion(models.Model):
    id = models.AutoField(primary_key = True)
    imagen = models.URLField(max_length = 255, blank = False, null= False, default="https://www.parkpiolets.com/content/imgsxml/galerias/panel_habitaciones/6/des-0016-pioletspark-doblepremium320.jpg")
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, null=False)
    activo = models.BooleanField( default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Imagen Habitacion'
        verbose_name_plural = 'Imagenes de Habitacion'

    def __str__(self):
        return self.habitacion

class Comodidad(models.Model):
    id = models.AutoField(primary_key = True)
    habitaciones = models.ManyToManyField(Habitacion)
    nombre = models.CharField(max_length = 100, null = False,blank = False)
    descripcion = models.CharField(max_length = 110, blank = False, null = False)
    activo = models.BooleanField( default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Comodidad'
        verbose_name_plural = 'Comodidades'

    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    id = models.AutoField(primary_key = True)
    usuario = models.OneToOneField(Usuario,on_delete=models.DO_NOTHING)
    habitaciones = models.ManyToManyField(Habitacion)
    diaInicio = models.DateField(null = False,blank = False)
    diaFin = models.DateField(null = False,blank = False)
    activo = models.BooleanField( default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return self.usuario


class Factura(models.Model):
    id = models.AutoField(primary_key = True)
    reserva = models.OneToOneField(Reserva,on_delete=models.DO_NOTHING)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    descuento = models.DecimalField(max_digits=20, decimal_places=2)
    activo = models.BooleanField( default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return self.total

