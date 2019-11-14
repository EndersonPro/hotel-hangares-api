# from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Usuario, Habitacion, ImagenHabitacion, TipoHabitacion, Reserva, HabitacionReservada, Comodidad, Factura


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['id','username','password','cedula','email','phone', 'last_name','first_name',
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

class WriteHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ['id','numero','tipoHabitacion','piso','descripcion','precio','reservada','activo','creado']


class ReadHabitacionSerializer(serializers.ModelSerializer):
    tipoHabitacion = TipoHabitacionSerializer()
    class Meta:
        model = Habitacion
        fields = ['id','numero','tipoHabitacion','piso','descripcion','precio','reservada','activo','creado']


class ImagenHabitacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImagenHabitacion
        fields = ['id', 'imagen', 'habitacion', 'activo', 'creado']

class ReadReservaSerializer(serializers.ModelSerializer):
    responsable = UsuarioSerializer()
    usuario = UsuarioSerializer()
    habitaciones = ReadHabitacionSerializer(many=True)
    class Meta:
        model = Reserva
        fields = ['id', 'responsable', 'usuario', 'habitaciones', 'fechaInicio', 'fechaFin','activo','creado']

class WriteReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = ['id', 'responsable', 'usuario', 'habitaciones', 'fechaInicio', 'fechaFin','activo','creado']

class HabitacionReservadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = HabitacionReservada
        fields = ['id', 'reserva', 'habitacion', 'precioVenta', 'activo', 'creado']

class ComodidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comodidad
        fields = ['id', 'habitaciones', 'nombre', 'descripcion','activo','creado']

class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = ['id', 'reserva', 'fecha', 'descuento','activo','creado']

