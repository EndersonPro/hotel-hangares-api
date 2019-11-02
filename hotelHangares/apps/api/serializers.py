# from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Usuario, Habitacion, TipoHabitacion, Reserva, HabitacionAsignada, Comodidad, Factura


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['id','username','password','email','last_name','first_name',
                  'tipoUsuario', 'foto_perfil']
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class TipoHabitacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoHabitacion
        fields = ['id', 'nombre', 'descripcion','activo','creado']

class HabitacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Habitacion
        fields = ['id','numero','tipoHabitacion','piso','descripcion','precio','activo','creado']

class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = ['id', 'responsable', 'usuario', 'habitaciones', 'fechaInicio', 'fechaFin','activo','creado']

class HabitacionAsignadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = HabitacionAsignada
        fields = ['id', 'reserva', 'habitacion', 'precioVenta', 'activo', 'creado']

class ComodidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comodidad
        fields = ['id', 'habitaciones', 'nombre', 'descripcion','activo','creado']

class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = ['id', 'reserva', 'fecha', 'descuento','activo','creado']

