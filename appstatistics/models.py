from django.db import models


class Amplua(models.Model):
    amplua = models.CharField(max_length=45)

    def __str__(self):
        return self.amplua


class Block(models.Model):
    type_block = models.ForeignKey('TypeBlock', models.DO_NOTHING, db_column='Type_block_id', blank=True,
                                   null=True)  # Field name made lowercase.
    player_statistic_on_set = models.ForeignKey('PlayerStatisticOnSet', models.DO_NOTHING,
                                                db_column='Player_statistic_on_set_id')  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)


class Card(models.Model):
    color = models.CharField(max_length=45)

    def __str__(self):
        return self.color


class Coach(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    def __str__(self):
        return f'{self.user.name} {self.user.surname}'


class GameMistake(models.Model):
    mistake = models.CharField(max_length=45)

    def __str__(self):
        return self.mistake


class Judge(models.Model):
    category = models.CharField(max_length=100)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    def __str__(self):
        return f'{self.user.name} {self.user.surname}'


class League(models.Model):
    league = models.CharField(max_length=100)

    def __str__(self):
        return self.league


class Match(models.Model):
    tournament = models.ForeignKey('Tournament', models.DO_NOTHING,
                                   db_column='Tournament_id')  # Field name made lowercase.
    stage = models.ForeignKey('Stage', models.DO_NOTHING, db_column='Stage_id', blank=True,
                              null=True)  # Field name made lowercase.
    matches_place = models.ForeignKey('MatchPlace', models.DO_NOTHING,
                                      db_column='Matches_place_id')  # Field name made lowercase.
    date = models.DateTimeField()


class MatchHasJudge(models.Model):
    judge = models.ForeignKey(Judge, models.DO_NOTHING, db_column='Judge_id')  # Field name made lowercase.
    match = models.ForeignKey(Match, models.DO_NOTHING, db_column='Match_id')  # Field name made lowercase.
    type = models.CharField(max_length=100)


class MatchPlace(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Media(models.Model):
    type = models.CharField(max_length=45)

    def __str__(self):
        return self.type


class Team(models.Model):
    team_type = models.ForeignKey('TypeTeam', models.DO_NOTHING, db_column='Team_type_id', blank=True,
                                  null=True)  # Field name made lowercase.
    coach = models.ForeignKey(Coach, models.DO_NOTHING, db_column='Coach_id', blank=True,
                              null=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)
    photo = models.ImageField(upload_to='images/', null=True)
    logo = models.CharField(max_length=150, blank=True, null=True)
    date_foundation = models.TextField(blank=True, null=True)  # This field type is a guess.
    sponsor = models.CharField(max_length=100, blank=True, null=True)
    sponsor_logo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    amplua = models.ForeignKey(Amplua, models.DO_NOTHING, db_column='Amplua_id', blank=True,
                               null=True)  # Field name made lowercase.
    team = models.ForeignKey('Team', models.DO_NOTHING, db_column='Team_id')  # Field name made lowercase.
    height = models.IntegerField(blank=True, null=True)
    height_level = models.IntegerField(blank=True, null=True)
    game_number = models.IntegerField(blank=True, null=True)
    is_captain = models.BooleanField(blank=True, null=True, default=False)
    is_leader = models.BooleanField(blank=True, null=True, default=False)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.

    def __str__(self):
        return f'{self.team.name} - {self.user.surname} {self.user.name}'


class PlayerHasCards(models.Model):
    card = models.ForeignKey(Card, models.DO_NOTHING, db_column='Card_id')  # Field name made lowercase.
    player_statistic_on_set = models.ForeignKey('PlayerStatisticOnSet', models.DO_NOTHING,
                                                db_column='Player_statistic_on_set_id')  # Field name made lowercase.
    time = models.DateTimeField(auto_now_add=True)


class PlayerHasMatch(models.Model):
    match = models.ForeignKey(Match, models.DO_NOTHING, db_column='Match_id')  # Field name made lowercase.
    player = models.ForeignKey(Player, models.DO_NOTHING, db_column='Player_id')  # Field name made lowercase.
    amplua = models.ForeignKey(Amplua, models.DO_NOTHING, db_column='Amplua_id', blank=True,
                               null=True)  # Field name made lowercase.
    game_number = models.IntegerField(blank=True, null=True)


class PlayerHasMistake(models.Model):
    game_mistake = models.ForeignKey(GameMistake, models.DO_NOTHING,
                                     db_column='Game_mistake_id')  # Field name made lowercase.
    player_statistic_on_set = models.ForeignKey('PlayerStatisticOnSet', models.DO_NOTHING,
                                                db_column='Player_statistic_on_set_id')  # Field name made lowercase.
    time = models.DateTimeField(auto_now_add=True)


class PlayerStatisticOnSet(models.Model):
    set = models.ForeignKey('Set', models.DO_NOTHING, db_column='Set_id')  # Field name made lowercase.
    player = models.ForeignKey(Player, models.DO_NOTHING, db_column='Player_id')  # Field name made lowercase.


class Receiving(models.Model):
    type_receiving = models.ForeignKey('TypeReceiving', models.DO_NOTHING, db_column='Type_receiving_id', blank=True,
                                       null=True)  # Field name made lowercase.
    player_statistic_on_set = models.ForeignKey(PlayerStatisticOnSet, models.DO_NOTHING,
                                                db_column='Player_statistic_on_set_id')  # Field name made lowercase.
    time = models.DateTimeField()


class Role(models.Model):
    role = models.CharField(max_length=45)


class Service(models.Model):
    type_service = models.ForeignKey('TypeService', models.DO_NOTHING, db_column='Type_service_id', blank=True,
                                     null=True)  # Field name made lowercase.
    player_statistic_on_set = models.ForeignKey(PlayerStatisticOnSet, models.DO_NOTHING,
                                                db_column='Player_statistic_on_set_id')  # Field name made lowercase.
    is_ace = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    x_from = models.FloatField(blank=True, null=True)
    y_from = models.FloatField(blank=True, null=True)
    x_to = models.FloatField(blank=True, null=True)
    y_to = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)


class Set(models.Model):
    match = models.ForeignKey(Match, models.DO_NOTHING, db_column='Match_id')  # Field name made lowercase.
    number = models.IntegerField()
    score = models.IntegerField(blank=True, null=True)


class Spike(models.Model):
    type_spike = models.ForeignKey('TypeSpike', models.DO_NOTHING, db_column='Type_spike_id', blank=True,
                                   null=True)  # Field name made lowercase.
    player_statistic_on_set = models.ForeignKey(PlayerStatisticOnSet, models.DO_NOTHING,
                                                db_column='Player_statistic_on_set_id')  # Field name made lowercase.
    is_point = models.IntegerField()
    is_out = models.IntegerField(blank=True, default=False)
    in_net = models.IntegerField(blank=True, default=False)
    x_from = models.IntegerField(blank=True, null=True)
    y_from = models.IntegerField(blank=True, null=True)
    x_to = models.IntegerField(blank=True, null=True)
    y_to = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)


class Stage(models.Model):
    stage = models.CharField(max_length=100)

    def __str__(self):
        return self.stage


class Subgroup(models.Model):
    subgroup = models.CharField(max_length=50)

    def __str__(self):
        return self.subgroup


class TeamOnMatch(models.Model):
    match = models.ForeignKey(Match, models.DO_NOTHING, db_column='Match_id')  # Field name made lowercase.
    team = models.ForeignKey(Team, models.DO_NOTHING, db_column='Team_id')  # Field name made lowercase.
    score = models.IntegerField(db_column='Score')  # Field name made lowercase.


class TeamOnTournament(models.Model):
    tournament = models.ForeignKey('Tournament', models.DO_NOTHING,
                                   db_column='Tournament_id')  # Field name made lowercase.
    team = models.ForeignKey(Team, models.DO_NOTHING, db_column='Team_id')  # Field name made lowercase.
    league = models.ForeignKey(League, models.DO_NOTHING, db_column='League_id', blank=True,
                               null=True)  # Field name made lowercase.
    subgroup = models.ForeignKey(Subgroup, models.DO_NOTHING, db_column='Subgroup_id', blank=True,
                                 null=True)  # Field name made lowercase.
    place = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.tournament.name}: {self.team.name}'


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name


class TypeBlock(models.Model):
    type = models.CharField(max_length=100)


class TypeReceiving(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class TypeService(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class TypeSpike(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class TypeTeam(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class User(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING, db_column='Role_id', blank=True,
                             null=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    login = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname} {self.middle_name}'


class UserHasMedia(models.Model):
    media = models.OneToOneField(Media, models.DO_NOTHING, db_column='Media_id',
                                 primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    link = models.CharField(max_length=100)
