from django.db import models
from cms.models import CMSPlugin
from community.models import Clan, Member, Game
from django.utils.translation import ugettext as _

class Match(models.Model):
	datetime = models.DateTimeField(_("Date"))
	game = models.ForeignKey(Game, verbose_name=_("Game"))
	clanA = models.ForeignKey(Clan, related_name="clanA_set")
	clanB = models.ForeignKey(Clan, related_name="clanB_set")
	winner = models.ForeignKey(Clan, null=True, blank=True)
	def __unicode__(self):
		return "%s vs %s" % (self.clanA, self.clanB)

class MemberScore(models.Model):
	match = models.ForeignKey(Match, verbose_name=_("Match"))
	player = models.ForeignKey(Member, verbose_name=_("Player"))
	kills = models.IntegerField(_("Kills"), null=True, blank=True)
	deaths = models.IntegerField(_("Deaths"), null=True, blank=True)
	assists = models.IntegerField(_("Assists"), null=True, blank=True)

class LastMatchesPlugin(CMSPlugin):
	amount = models.IntegerField(_("Aantal"))