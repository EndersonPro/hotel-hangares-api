# from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from .serializers import UsuarioSerializer, ChangePasswordSerializer, ReadHabitacionSerializer,WriteHabitacionSerializer, ImagenHabitacionSerializer, WriteReservaSerializer, ReadReservaSerializer, HabitacionReservadaSerializer, ComodidadSerializer, TipoHabitacionSerializer, FacturaSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework.decorators import action
from .models import Usuario, Habitacion, ImagenHabitacion, Reserva, HabitacionReservada, Comodidad, TipoHabitacion, Factura
from .mixins import ReadWriteSerializerMixin

from .permissions import IsReceptionist, IsClient, IsAdmin


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes_by_action = {
        'create': [AllowAny],
        'list': [IsAdmin|IsReceptionist],
        'update': [IsAdmin | IsClient]
    }
    # permission_classes = (IsAuthenticated,)
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):

        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    def perform_update(self, serializer):

        if "password" in self.request.data.keys():
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    def get_queryset(self):
        cedula = self.request.query_params.get('cedula')
        if cedula:
            return Usuario.objects.filter(cedula=cedula)
        else:
            return Usuario.objects.all()

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class ChangePasswordView(viewsets.ModelViewSet):

    serializer_class = ChangePasswordSerializer
    model = Usuario
    queryset = Usuario.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password"]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TipoHabitacionViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer


class HabitacionViewSet(ReadWriteSerializerMixin, viewsets.ModelViewSet):

    permission_classes_by_action = {
        'create': [IsAdmin],
        'list': [AllowAny],
        'update': [IsAdmin|IsReceptionist]
    }
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Habitacion.objects.all()
    read_serializer_class = ReadHabitacionSerializer
    write_serializer_class = WriteHabitacionSerializer

    def get_queryset(self):
        reservada = self.request.query_params.get('reservada')
        tipoHabitacion = self.request.query_params.get('tipoHabitacion')
        fechaInicio = self.request.query_params.get('fechaInicio')
        fechaFin = self.request.query_params.get('fechaFin')
        if fechaInicio and fechaFin:
            reservas = Reserva.objects.all().filter(Q(fechaInicio__range=[fechaInicio, fechaFin]) & Q(estado = 1) |
                                          Q(fechaFin__range=[fechaInicio, fechaFin]) & Q(estado = 1))
            keys = []
            for r in reservas.iterator():
                for h in r.habitaciones.iterator():
                    keys.append(h.id)
            return Habitacion.objects.exclude(id__in=keys)
        elif reservada and tipoHabitacion:
            return Habitacion.objects.filter(reservada=reservada, tipoHabitacion=tipoHabitacion)
        elif reservada:
            return Habitacion.objects.filter(reservada=reservada) 
        elif tipoHabitacion:
            return Habitacion.objects.filter(tipoHabitacion=tipoHabitacion)
        else:
            return Habitacion.objects.all()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ImagenHabitacionViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ImagenHabitacion.objects.all()
    serializer_class = ImagenHabitacionSerializer

    def get_queryset(self):
        habitacion = self.request.query_params.get('habitacion')
        if habitacion:
            return ImagenHabitacion.objects.filter(habitacion=habitacion)
        else:
            return ImagenHabitacion.objects.all()


class ReservaViewSet(ReadWriteSerializerMixin,viewsets.ModelViewSet):

    permission_classes_by_action = {
        'create': [IsReceptionist|IsClient],
        'list': [AllowAny],
        'update': [IsReceptionist]
    }

    # permission_classes = (IsAuthenticated,)
    queryset = Reserva.objects.all()
    read_serializer_class = ReadReservaSerializer
    write_serializer_class = WriteReservaSerializer

    def get_queryset(self):
        fechaInicio = self.request.query_params.get('fechaInicio')
        fechaFin = self.request.query_params.get('fechaFin')
        if fechaInicio  and fechaFin:
            return Reserva.objects.filter(Q(fechaInicio__range=[fechaInicio, fechaFin]) & Q(estado = 1) |
                                          Q(fechaFin__range=[fechaInicio, fechaFin]) & Q(estado = 1))
        else:
            return Reserva.objects.all()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class HabitacionReservadaViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = HabitacionReservada.objects.all()
    serializer_class = HabitacionReservadaSerializer

    def get_queryset(self):
        reserva = self.request.query_params.get('reserva')
        if reserva:
            return HabitacionReservada.objects.filter(reserva=reserva)
        else:
            return HabitacionReservada.objects.all()


class ComodidadViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Comodidad.objects.all()
    serializer_class = ComodidadSerializer


class FacturaViewSet(viewsets.ModelViewSet):

    permission_classes_by_action = {
        'create': [IsReceptionist|IsAdmin],
        'list': [IsReceptionist|IsClient],
        'update': [IsReceptionist|IsAdmin]
    }

    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]