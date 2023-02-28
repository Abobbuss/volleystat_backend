
from rest_framework import serializers
from .models import Team, TypeTeam, Coach, User, TeamOnTournament, Tournament
from django.forms import model_to_dict


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'id_user': instance.user.id,
            'role': instance.user.role,
            'name': instance.user.name,
            'surname': instance.user.surname,
            'middle_name': instance.user.middle_name,
            'age': instance.user.age,
            'photo': instance.user.photo,
            'gender': instance.user.gender,
            'login': instance.user.login,
            'password': instance.user.password,
            'category': instance.category
        }

class TeamsSerializer(serializers.ModelSerializer):
    coach = CoachSerializer()
    class Meta:
        model = Team
        fields = '__all__'


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class TeamOnTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamOnTournament
        fields ='__all__'

