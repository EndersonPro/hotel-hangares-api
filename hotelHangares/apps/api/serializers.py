from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Usuario
import threading


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['id','username', 'password', 'email','last_name','first_name',
                  'tipoUsuario', 'foto_perfil']
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = ['nombre', 'password', 'correo','imagen']
