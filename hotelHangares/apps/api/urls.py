from django.urls import path, include
from .api import UsuarioViewSet, ChangePasswordView, HabitacionViewSet, ImagenHabitacionViewSet, ReservaViewSet, HabitacionReservadaViewSet, ComodidadViewSet, TipoHabitacionViewSet, FacturaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
# TODO: Hay un problema con las rutas de users y de change password, 
router.register(r'changepassword', ChangePasswordView)
router.register(r'users', UsuarioViewSet)
router.register(r'rooms', HabitacionViewSet)
router.register(r'imagerooms', ImagenHabitacionViewSet)
router.register(r'typerooms', TipoHabitacionViewSet)
router.register(r'comfort', ComodidadViewSet)
router.register(r'reserves', ReservaViewSet)
router.register(r'reservedrooms', HabitacionReservadaViewSet)
router.register(r'bills', FacturaViewSet)

urlpatterns = [
   path('', include(router.urls))
]
