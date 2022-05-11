from .models import *
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)
    mode = serializers.StringRelatedField(many=True)
    platforms = serializers.StringRelatedField(many=True)
    screenshot = serializers.StringRelatedField(many=True)
    company = serializers.StringRelatedField(many=False)
    franchise = serializers.StringRelatedField(many=False)
    release_date = serializers.SerializerMethodField('change_date')

    class Meta:
        model = Game
        fields ='__all__'

    def change_date(self, obj):
        return obj.release_date.strftime("%b %d, %Y")

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

class FavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fav
        fields ='__all__'


