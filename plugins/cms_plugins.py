from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import TwitchStreamPlugin, LikeBoxPlugin, TwitchChatPlugin
from django.utils.translation import ugettext as _

class CMSLoginRegisterPlugin(CMSPluginBase):
    name = _("Login/Register")
    render_template = "plugins/login_register.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object':instance,
            'placeholder':placeholder
        })
        return context

class CMSTwitchStreamPlugin(CMSPluginBase):
    model = TwitchStreamPlugin
    name = _("Twitch Stream")
    render_template = "plugins/twitch_stream.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object':instance,
            'placeholder':placeholder
        })
        return context

class CMSTwitchChatPlugin(CMSPluginBase):
    model = TwitchChatPlugin
    name = _("Twitch Chat")
    render_template = "plugins/twitch_chat.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object':instance,
            'placeholder':placeholder
        })
        return context

class CMSLikeBoxPlugin(CMSPluginBase):
    model = LikeBoxPlugin
    name = _("Like Box")
    render_template = "plugins/like_box.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSLoginRegisterPlugin)
plugin_pool.register_plugin(CMSTwitchStreamPlugin)
plugin_pool.register_plugin(CMSTwitchChatPlugin)
plugin_pool.register_plugin(CMSLikeBoxPlugin)