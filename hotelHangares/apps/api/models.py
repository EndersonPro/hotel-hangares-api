from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.utils import timezone

# Create your models here.

class TipoUsuario(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, null = False,blank = False)
    descripcion = models.CharField(max_length = 110, blank = False, null = False)
    activo = models.BooleanField(default = True)
    # al final no nos importa mucho cuando se creo el tipo de usuario
    creado = models.DateField(default = timezone.now)

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
    cedula = models.IntegerField(blank = False, null=False, default=123, unique=True)
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.DO_NOTHING, null=False, default=3)
    foto_perfil = models.URLField(max_length = 255, blank = False, null= False, default="https://www.info-computer.com/blog/wp-content/uploads/2018/04/fotoinicio.jpg")
    phone = models.IntegerField(blank = True, null=True)
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"

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
    reservada = models.BooleanField(default = False)
    activo = models.BooleanField( default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'

    def __str__(self):
        return f"{self.numero}"

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
        return f"{self.habitacion}"

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
    
class EstadoReserva(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, null = False,blank = False)
    descripcion = models.CharField(max_length = 110, blank = False, null = False)
    activo = models.BooleanField(default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Estado de Reserva'
        verbose_name_plural = 'Estados de Reservas'

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    id = models.AutoField(primary_key = True)
    responsable = models.ForeignKey(Usuario, related_name='responsable',on_delete=models.DO_NOTHING, null=False)
    usuario = models.ForeignKey(Usuario, related_name='cliente', on_delete=models.DO_NOTHING, null =False)
    habitaciones = models.ManyToManyField(Habitacion, through='HabitacionReservada')
    fechaInicio = models.DateField(null = False,blank = False)
    fechaFin = models.DateField(null = False,blank = False)
    estado = models.ForeignKey(EstadoReserva, on_delete = models.DO_NOTHING, null = True)
    activo = models.BooleanField( default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f"{self.usuario} el {self.fechaInicio} hasta el {self.fechaFin}"

class HabitacionReservada(models.Model):
    id = models.AutoField(primary_key = True)
    reserva = models.ForeignKey(Reserva, on_delete=models.DO_NOTHING)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.DO_NOTHING)
    precioVenta = models.DecimalField(max_digits=20, decimal_places=2)
    activo = models.BooleanField( default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    # Trigger para cambiar estado de la habitacion asignada
    def save(self, *args, **kwargs):
        habitacion=Habitacion.objects.get(id=self.habitacion.id)
        habitacion.reservada = True
        habitacion.save()
        return super(HabitacionReservada, self).save( *args, **kwargs)

    def delete(self, *args, **kwargs):
        habitacion=Habitacion.objects.get(id=self.habitacion.id)
        habitacion.reservada = False
        habitacion.save()
        return super(HabitacionReservada, self).delete( *args, **kwargs)

    class Meta:
        verbose_name = 'Habitacion Asignada'
        verbose_name_plural = 'Habitaciones Asignadas'

    def __str__(self):
        return f"Habitacion:{self.habitacion}, Reserva: {self.reserva}"


class Factura(models.Model):
    id = models.AutoField(primary_key = True)
    reserva = models.OneToOneField(Reserva,on_delete=models.DO_NOTHING)
    fecha = models.DateField(null = False,blank = False)
    descuento = models.DecimalField(max_digits=20, decimal_places=2)
    activo = models.BooleanField( default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return f"{self.id} {self.fecha}"