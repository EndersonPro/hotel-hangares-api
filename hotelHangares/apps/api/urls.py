from django.urls import path, include
from .api import UsuarioViewSet, ChangePasswordView, HabitacionViewSet, ReservaViewSet, HabitacionReservadaViewSet, ComodidadViewSet, TipoHabitacionViewSet, FacturaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UsuarioViewSet)
router.register(r'changepassword', ChangePasswordView)
router.register(r'rooms', HabitacionViewSet)
router.register(r'typerooms', TipoHabitacionViewSet)
router.register(r'comfort', ComodidadViewSet)
router.register(r'reserves', ReservaViewSet)
router.register(r'reservedrooms', HabitacionReservadaViewSet)
router.register(r'bills', FacturaViewSet)

urlpatterns = [
   path('', include(router.urls))
]
