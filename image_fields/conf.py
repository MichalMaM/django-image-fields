from importlib import import_module

from django.conf import settings as dj_settings
from django.core.exceptions import ImproperlyConfigured


class Settings(object):

    def __init__(self, module_name, prefix=''):
        self.module = import_module(module_name)
        self.prefix = prefix

    def __getattr__(self, name):
        p_name = '%s_%s' % (self.prefix, name) if self.prefix else name

        if hasattr(dj_settings, p_name):
            return getattr(dj_settings, p_name)

        try:
            return getattr(self.module, name)
        except AttributeError:
            raise ImproperlyConfigured("'%s' setting doesn't exist in your settings module '%s'." % (
                p_name,
                self.module.__name__
            ))

    def __dir__(self):
        return dir(self.module) + dir(dj_settings)


DEFAULT_IMAGE_SIZE = (800, 800)
DEFAULT_IMAGE_QUALITY = 98

settings = Settings('image_fields.conf', 'IMAGE_FIELDS')
