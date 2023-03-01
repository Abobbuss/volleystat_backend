from rest_framework import routers
from appstatistics import views

routerTeams = routers.SimpleRouter()
routerTeams.register(r'teams', views.TeamAPIViewSet)

routerTeamOnTournament = routers.SimpleRouter()
routerTeamOnTournament.register(r'teamOnTournaments', views.TeamOnTournamentAPIViewSet)

routerUser = routers.SimpleRouter()
routerUser.register(r'user', views.UserAPIViewSet)
