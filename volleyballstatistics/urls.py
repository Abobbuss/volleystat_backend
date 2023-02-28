"""volleyballstatistics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appstatistics.views import index, TeamAPIView, CoachAPIView, UserAPIView, TeamOnTournamentAPIView, \
    TournamentAPIView
from drf_yasg.views import get_schema_view as swagger_get_shema_view
from drf_yasg import openapi

shema_view = swagger_get_shema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API documentation of App"
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teams/', index),
    path('api/v1/',
         include([
             path('swagger/shema/', shema_view.with_ui('swagger', cache_timeout=0)),#Все апишки
             path('teams/', TeamAPIView.as_view()),#Все команды
             path('coach/<int:pk>/', CoachAPIView.as_view()),#Тренер с определенным pk = id
             path('user/<int:pk>/', UserAPIView.as_view()),#Юзер с определенным pk = id
             path('tournaments', TournamentAPIView.as_view()),
             path('teamontournament/', TeamOnTournamentAPIView.as_view())
         ])),

]
