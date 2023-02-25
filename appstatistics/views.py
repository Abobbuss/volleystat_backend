from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Team, Coach, User, TeamOnTournament
from .serializers import TeamsSerializer, CoachSerializer, UserSerializer, TeamOnTournamentSerializer


def index(request):
    return render(request, 'appstatistics/index.html')


class TeamAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamsSerializer


class CoachAPIView(generics.ListAPIView):
    serializer_class = CoachSerializer
    queryset = Coach.objects.all()

    def get(self, request, pk):
        coach = Coach.objects.get(id=pk)
        serializer = CoachSerializer(coach)
        return Response(serializer.data)


class UserAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class TeamOnTournamentAPIView(APIView):
    queryset = Team.objects.all()
    serializer_class = TeamOnTournamentSerializer

    def get(self, request):
        teamOnTournament_new = TeamOnTournament.objects.all().values()
        return Response({'teamOnTournament': list(teamOnTournament_new)})

    def post(self, request):
        teamOnTournament_new = TeamOnTournament.objects.create(
            tournament=request.data['tournament'],
            team=request.data['team'],
            league=request.data['league'],
            subgroup=request.data['subgroup'],
            place=request.data['place']
        )
        return Response({'post': model_to_dict(teamOnTournament_new)})

