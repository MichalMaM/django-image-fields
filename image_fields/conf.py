from django.conf import settings

DEFAULT_IMAGE_SIZE = getattr(settings, 'IMAGE_FIELDS_DEFAULT_IMAGE_SIZE', (800, 800))
DEFAULT_IMAGE_QUALITY = getattr(settings, 'IMAGE_FIELDS_DEFAULT_IMAGE_QUALITY', 98)
