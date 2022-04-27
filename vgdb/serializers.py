from .models import *
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields ='__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields ='__all__'

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields ='__all__'

class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields ='__all__'

class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields ='__all__'


