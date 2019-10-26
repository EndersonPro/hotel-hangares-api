"""hotelHangares URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from apps.AdminHotel import api
from rest_framework_simplejwt.views import TokenRefreshView
from .jwt import *


router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'groups', api.GroupViewSet)

urlpatterns = [
    path('', admin.site.urls),
    path('api/v1.0/', include(router.urls)),
    path('api/v1.0/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1.0/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', include(('apps.AdminHotel.urls', 'adminHotel'))),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
