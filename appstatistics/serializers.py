from rest_framework import serializers
from . import models
from django.forms import model_to_dict


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coach
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
            'category': instance.category
        }


class TeamsSerializer(serializers.ModelSerializer):
    coach = CoachSerializer()

    class Meta:
        model = models.Team
        fields = '__all__'


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tournament
        fields = '__all__'


class TeamsOnTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamOnTournament
        fields = '__all__'

    def to_representation(self, instance):
        if instance.league or instance.subgroup is None:
            if instance.league is None and instance.subgroup is None:
                Subgroup = None
                League = None
            if instance.league is None and instance.subgroup is not None:
                Subgroup = instance.subgroup.subgroup
                League = None
            if instance.league is not None and instance.subgroup is None:
                Subgroup = None
                League = instance.league.league
        else:
            Subgroup = instance.subgroup.subgroup
            League = instance.league.league
        return {
            'id': instance.id,
            'id_team': instance.team.id,
            'team': instance.team.name,
            'league': League,
            'subgroup': Subgroup,
            'place': instance.place,
        }


class TeamOnTournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamOnTournament
        fields = "__all__"

    def to_representation(self, instance):
        if instance.league or instance.subgroup is None:
            if instance.league is None and instance.subgroup is None:
                Subgroup = None
                League = None
            if instance.league is None and instance.subgroup is not None:
                Subgroup = instance.subgroup.subgroup
                League = None
            if instance.league is not None and instance.subgroup is None:
                Subgroup = None
                League = instance.league.league
        else:
            Subgroup = instance.subgroup.subgroup
            League = instance.league.league
        return {
            'id': instance.id,
            'id_team': instance.team.id,
            'team': instance.team.name,
            'league': League,
            'subgroup': Subgroup,
            'place': instance.place,
        }


