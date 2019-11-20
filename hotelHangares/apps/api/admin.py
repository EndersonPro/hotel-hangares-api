from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register(Usuario, UserAdmin)
admin.site.register(TipoUsuario)
admin.site.register(TipoHabitacion)
admin.site.register(Habitacion)
admin.site.register(EstadoReserva)
admin.site.register(Reserva)
admin.site.register(HabitacionReservada)
admin.site.register(Factura)
admin.site.register(Comodidad)
admin.site.register(ImagenHabitacion)


