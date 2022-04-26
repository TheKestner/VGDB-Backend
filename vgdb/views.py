from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import GameSerializer
from .models import *

# Create your views here.

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow games to be viewed.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

