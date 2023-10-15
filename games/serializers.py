from rest_framework import serializers
from .models import Games



class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['id', "name", "price", 'about']

