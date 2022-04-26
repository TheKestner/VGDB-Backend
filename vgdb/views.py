from django.shortcuts import render
from resst_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *

# Create your views here.

class GameViewSet(viewsets.ModelViewSets):
    """
    API endpoint that allow games to be viewed.
    """
    queryset = Game.objects.all()
    serializers_class = GameSerializer

