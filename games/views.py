from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GamesSerializer
from .models import Games
from rest_framework.permissions import IsAuthenticated



class GamesListApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        games = Games.objects.all()
        serializer = GamesSerializer(games, many=True)

        return Response(serializer.data)


class GamesDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        game = Games.objects.get(id=id)
        serializer = GamesSerializer(game)

        return Response(serializer.data)





