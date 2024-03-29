import pkg_resources
from importlib import import_module
from django.template import Library
# from django.apps.apps import get_model
from django.apps import apps
from django.utils.safestring import SafeText

from ..utils import implements as base_implements
from ..utils import object_to_urn as utils_object_to_urn

register = Library()


MESSAGE_LEVELS = {
    10: "debug",
    20: "info",
    25: "success",
    30: "warning",
    40: "error"
}


@register.inclusion_tag('djinn_core/snippets/css.html')
def list_plugin_css(static_url):

    css = []

    for entrypoint in pkg_resources.iter_entry_points(group="djinn.app",
                                                      name="css"):
        css.extend(entrypoint.load()())

    def mkcss(link):

        props = {'media': 'screen'}

        if not isinstance(link, str):
            props['href'] = link[0]
            if len(link) > 1:
                props['media'] = link[1]
        else:
            props['href'] = link

        return props

    # MJB map
    css = [mkcss(lnk) for lnk in css]

    return {"plugin_css": css, "STATIC_URL": static_url}


@register.inclusion_tag('djinn_core/snippets/js.html')
def list_plugin_js(static_url):

    js = []

    for entrypoint in pkg_resources.iter_entry_points(group="djinn.app",
                                                      name="js"):
        js.extend(entrypoint.load()())

    return {"plugin_js": js, "STATIC_URL": static_url}


@register.filter(name="messageclass")
def messageclass(messages):

    """ Filter level from messages and return str representation """

    if len(messages):
        try:
            level = messages._loaded_messages[0].level
        except:
            level = messages._queued_messages[0].level
    else:
        level = 20

    return MESSAGE_LEVELS.get(level, "info")


@register.filter
def implements(instance, clazz):

    """ instance should be an object instance; clazz should be the
    full dotted name of the class, or an actual class, or a model specified
    as <app>.<model> """

    if isinstance(clazz, SafeText):

        parts = clazz.split(".")

        if len(parts) == 2:
            clazz = apps.get_model(*parts)
        else:
            clazz = getattr(import_module(".".join(parts[:-1])), parts[-1])

    return base_implements(instance, clazz)


@register.simple_tag
def object_to_urn(object):
    return utils_object_to_urn(object)


@register.inclusion_tag('gronet_v3/includes/okay_notokay_icon.html')
def okay_notokay_icon(okay):
    return {"show_okay": okay}
