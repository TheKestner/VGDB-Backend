from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import GameSerializer, GenreSerializer, PlatformSerializer, ModeSerializer, ScreenshotSerializer
from .models import *

# Create your views here.

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow games to be viewed.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow games to be viewed.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow games to be viewed.
    """
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class ModeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow games to be viewed.
    """
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer

class ScreenshotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow games to be viewed.
    """
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer

