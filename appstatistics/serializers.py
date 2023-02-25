
from rest_framework import serializers
from .models import Team, TypeTeam, Coach, User, TeamOnTournament


class TeamsSerializer(serializers.ModelSerializer):
    team_type = serializers.SlugRelatedField(slug_field="type", read_only=True)
    class Meta:
        model = Team
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TeamOnTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamOnTournament
        fields ='__all__'

