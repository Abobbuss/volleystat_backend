from django.forms import model_to_dict
from django.shortcuts import render
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

    def get(self, request, pk):
        user = models.User.objects.get(id=pk)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)


class TournamentAPIView(generics.ListAPIView):
    serializer_class = serializers.TournamentSerializer
    queryset = models.Tournament.objects.all()

    def list(self, request, *args, **kwargs):
        res = super(TournamentAPIView, self).list(request, *args, **kwargs)
        res.data = {'data': res.data}
        return res


class TeamOnTournamentAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamOnTournamentSerializer


