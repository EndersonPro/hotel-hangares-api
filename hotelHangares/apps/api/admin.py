from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Habitacion)
admin.site.register(TipoHabitacion)
admin.site.register(Reserva)
admin.site.register(Factura)
admin.site.register(ImagenHabitacion)
admin.site.register(Comodidad)


