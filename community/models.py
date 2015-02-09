from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _

class Clan(models.Model):
	name = models.CharField(max_length=200)
	logo = models.ImageField(upload_to="uploads/logos/")
	def __unicode__(self):
		return self.name

class Member(AbstractUser):
	clan = models.ForeignKey(Clan, blank=True, null=True)

class Game(models.Model):
	name = models.CharField(max_length=200, unique=True)
	logo = models.ImageField(upload_to="uploads/logo/")
	wallpaper = models.ImageField(upload_to="uploads/wallpapers/")
	def __unicode__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=200, unique=True)
	def __unicode__(self):
		return self.name

class TeamRole(models.Model):
	name = models.CharField(max_length=200, unique=True)
	def __unicode__(self):
		return self.name

class TeamMember(models.Model):
	team = models.ForeignKey(Team, verbose_name=_("Team"))
	member = models.ForeignKey(Member, verbose_name=_("Member"))
	role = models.ForeignKey(TeamRole, verbose_name=_("Role"))
	def __unicode__(self):
		return "%s | %s - %s" % (self.team, self.member, self.role)

class Badge(models.Model):
	name = models.CharField(max_length=200, unique=True)
	icon = models.ImageField(upload_to="uploads/badges/")
	description = models.TextField()
	def __unicode__(self):
		return self.name

class BadgeOwner(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)
	member = models.ForeignKey(Member, verbose_name=_("Member"))
	badge = models.ForeignKey(Badge, verbose_name=_("Badge"))
	def __unicode__(self):
		return "%s | %s - %s" % (self.datetime, self.member, self.badge)