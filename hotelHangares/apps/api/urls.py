from django.urls import path, include
from .api import UsuarioViewSet, ChangePasswordView, HabitacionViewSet, ReservaViewSet, HabitacionAsignadaViewSet, ComodidadViewSet, TipoHabitacionViewSet, FacturaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UsuarioViewSet)
router.register(r'users/password', ChangePasswordView)
router.register(r'room', HabitacionViewSet)
router.register(r'room/types', TipoHabitacionViewSet)
router.register(r'comfort', ComodidadViewSet)
router.register(r'reserve', ReservaViewSet)
router.register(r'bill', FacturaViewSet)
router.register(r'bill/rooms', HabitacionAsignadaViewSet)

urlpatterns = [
   path('', include(router.urls))
]
