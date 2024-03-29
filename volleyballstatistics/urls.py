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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from appstatistics import views
from drf_yasg.views import get_schema_view as swagger_get_shema_view
from drf_yasg import openapi
from appstatistics import routers

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
    path('teams/', views.index),
    path('api/v1/',
         include([
             path('swagger/shema/', shema_view.with_ui('swagger', cache_timeout=0)),  # Все апишки
             path('', include(routers.routerTeams.urls)),
             path('coach/<int:pk>/', views.CoachAPIView.as_view()),
             path('', include(routers.routerUser.urls)),
             path('tournaments', views.TournamentAPIView.as_view()),
             path('tournament/<int:pk>/', views.TeamsOnTournamentAPIView.as_view()),
             path('tournament/<int:pk>/team/<int:pk2>/', views.TeamOnTournamentAPIView.as_view()),
             path('tournament/<int:pk>/subgroup/<int:pk2>/', views.SubgroupOnTournamentAPIView.as_view()),
             path('tournament/<int:pk>/league/<int:pk2>/', views.LeagueOnTournamentAPIView.as_view()),
             path('tournament/<int:pk>/league/<int:pk2>/subgroup/<int:pk3>/',
                  views.LeagueSubgroupOnTournamentAPIView.as_view()),
             path('accounts/', include('django.contrib.auth.urls')),
         ])),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
