from django.contrib import admin
from models import Match, MemberScore

class MemberScoreInline(admin.TabularInline):
	model = MemberScore

class MatchAdmin(admin.ModelAdmin):
	model = Match
	inlines = [MemberScoreInline,]

admin.site.register(Match, MatchAdmin)