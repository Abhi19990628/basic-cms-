from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import Person

class PersonPlugin(CMSPluginBase):
    name = _("Person Plugin")
    render_template = "person_plugin.html"

    def render(self, context, instance, placeholder):
        context['persons'] = Person.objects.all()  # Fetch all Person instances
        return context

plugin_pool.register_plugin(PersonPlugin)
