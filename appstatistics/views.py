from django.forms import model_to_dict
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets

from . import models
from . import serializers


def index(request):
    return render(request, 'appstatistics/index.html')


class TeamAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamsSerializer

    def list(self, request, *args, **kwargs):
        res = super(TeamAPIViewSet, self).list(request, *args, **kwargs)
        res.data = {'data': res.data}
        return res


class CoachAPIView(generics.ListAPIView):
    serializer_class = serializers.CoachSerializer
    queryset = models.Coach.objects.all()

    def get(self, request, pk):
        coach = models.Coach.objects.get(id=pk)
        serializer = serializers.CoachSerializer(coach)
        return Response(serializer.data)


class UserAPIViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()


class TournamentAPIView(generics.ListAPIView):
    serializer_class = serializers.TournamentSerializer
    queryset = models.Tournament.objects.all()

    def list(self, request, *args, **kwargs):
        res = super(TournamentAPIView, self).list(request, *args, **kwargs)
        res.data = {'data': res.data}
        return res


class TeamsOnTournamentAPIView(generics.ListAPIView):
    queryset = models.TeamOnTournament.objects.all()
    serializer_class = serializers.TeamsOnTournamentSerializer

    def get(self, request, pk):
        teams = models.TeamOnTournament.objects.filter(tournament=pk)
        serializer = serializers.TeamsOnTournamentSerializer(teams, many=True)
        return Response(serializer.data)


class TeamOnTournamentAPIView(generics.ListAPIView):
    queryset = models.TeamOnTournament.objects.all()
    serializer_class = serializers.TeamsOnTournamentSerializer

    def get(self, request, pk, pk2):
        team = models.TeamOnTournament.objects.get(tournament=pk, team=pk2)
        serializer = serializers.TeamsOnTournamentSerializer(team)
        return Response(serializer.data)


class SubgroupOnTournamentAPIView(generics.ListAPIView):
    queryset = models.TeamOnTournament.objects.all()
    serializer_class = serializers.TeamsOnTournamentSerializer

    def get(self, request, pk, pk2):
        teams = models.TeamOnTournament.objects.filter(tournament=pk, subgroup=pk2)
        serializer = serializers.TeamsOnTournamentSerializer(teams, many=True)
        return Response(serializer.data)


class LeagueOnTournamentAPIView(generics.ListAPIView):
    queryset = models.TeamOnTournament.objects.all()
    serializer_class = serializers.TeamsOnTournamentSerializer

    def get(self, request, pk, pk2):
        teams = models.TeamOnTournament.objects.filter(tournament=pk, league=pk2)
        serializer = serializers.TeamsOnTournamentSerializer(teams, many=True)
        return Response(serializer.data)


class LeagueSubgroupOnTournamentAPIView(generics.ListAPIView):
    queryset = models.TeamOnTournament.objects.all()
    serializer_class = serializers.TeamsOnTournamentSerializer

    def get(self, request, pk, pk2, pk3):
        teams = models.TeamOnTournament.objects.filter(tournament=pk, league=pk2, subgroup=3)
        serializer = serializers.TeamsOnTournamentSerializer(teams, many=True)
        return Response(serializer.data)
