from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import LastMatchesPlugin, Match
from django.utils.translation import ugettext as _

class CMSLastMatchesPlugin(CMSPluginBase):
    model = LastMatchesPlugin
    name = _("Last Matches")
    render_template = "matches/lastmatches.html"

    def render(self, context, instance, placeholder):
        context.update({
            'lastMatches': Match.objects.order_by('-datetime')[:instance.amount],
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSLastMatchesPlugin)