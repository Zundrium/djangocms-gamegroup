from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext as _

class TwitchStreamPlugin(CMSPlugin):
	name = models.CharField(_("Channel Name"), max_length=200)

class TwitchChatPlugin(CMSPlugin):
	name = models.CharField(_("Channel Name"), max_length=200)

class LikeBoxPlugin(CMSPlugin):
	name = models.CharField(_("Page Name"), max_length=200)