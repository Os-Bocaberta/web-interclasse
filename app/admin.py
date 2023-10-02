from django.contrib import admin
from .models import Teams, Players, PlayerModality, Match, TeamMatchInfo, Penalties, Rewards, Assistances

# Register your models here.

class TeamsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class PlayersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'instagram']

class PlayerModalityAdmin(admin.ModelAdmin):
    list_display = ['id', 'modality', 'activity', 'team', 'player']

class MatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'modality', 'status', 'start_time', 'winner']

class TeamMatchInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'team', 'match']

class PenaltiesAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'player', 'team_match']

class RewardsAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'player', 'team_match']

class AssistancesAdmin(admin.ModelAdmin):
    list_display = ['id', 'assist_to', 'player', 'team_match']

admin.site.register(Teams, TeamsAdmin)
admin.site.register(Players, PlayersAdmin)
admin.site.register(PlayerModality, PlayerModalityAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(TeamMatchInfo, TeamMatchInfoAdmin)
admin.site.register(Penalties, PenaltiesAdmin)
admin.site.register(Rewards, RewardsAdmin)
admin.site.register(Assistances, AssistancesAdmin)