"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import routers
from vgdb import views

router = routers.DefaultRouter()
router.register(r'game', views.GameViewSet)
router.register(r'genre', views.GenreViewSet)
router.register(r'platform', views.PlatformViewSet)
router.register(r'mode', views.ModeViewSet)
router.register(r'screenshot', views.ScreenshotViewSet)
router.register(r'fav', views.FavViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
