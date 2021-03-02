from django.contrib import admin
from .models import LeagueTeam, Player, Squad, Match, News
# Register your models here.
admin.site.register(News)

@admin.register(LeagueTeam)
class LeagueTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'points')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')

@admin.register(Squad)
class SquadAdmin(admin.ModelAdmin):
    list_display = ('role', 'full_name')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_number', 'host_team', 'host_team_score', 'guest_team_score', 'guest_team')