from django.contrib import admin
from models import Clan, Member, Game, Badge, BadgeOwner, Team, TeamMember, TeamRole

class ClanAdmin(admin.ModelAdmin):
	pass

class MemberAdmin(admin.ModelAdmin):
	pass

class BadgeAdmin(admin.ModelAdmin):
	pass

class BadgeOwnerAdmin(admin.ModelAdmin):
	pass

class TeamMemberInline(admin.TabularInline):
	model = TeamMember

class TeamAdmin(admin.ModelAdmin):
	inlines = [TeamMemberInline,]

class TeamRoleAdmin(admin.ModelAdmin):
	pass

admin.site.register(Clan, ClanAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Badge, BadgeAdmin)
admin.site.register(BadgeOwner, BadgeOwnerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamRole, TeamRoleAdmin)