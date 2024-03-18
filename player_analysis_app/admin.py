from django.contrib import admin
from .models import Team, Player, Stat, Accolade

#ONCE I HAVE REAL DATA, NEED TO CHANGE THESE VARIABLES AROUND

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'abbreviation', 'established')
    search_fields = ['name', 'city']

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'jersey_number', 'team', 'position')
    list_filter = ('team', 'position')
    search_fields = ['name']

class StatAdmin(admin.ModelAdmin):
    list_display = ('player', 'games_played', 'wins', 'losses', 'pts', 'reb', 'ast')
    list_filter = ('player', 'games_played')
    search_fields = ['player__name']

class AccoladeAdmin(admin.ModelAdmin):
    list_display = ('title', 'player', 'year')
    list_filter = ('year', 'player')
    search_fields = ('title', 'player__name')

admin.site.register(Accolade, AccoladeAdmin)

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(Accolade, AccoladeAdmin)

