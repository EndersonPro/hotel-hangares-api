from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','username', 'email','nombre',
                  'tipoUsuario', 'foto_perfil']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = ['nombre', 'password', 'correo','imagen']
