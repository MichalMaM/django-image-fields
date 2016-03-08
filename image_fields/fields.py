from django.db.models.fields.files import ImageField

from .forms import ResizedImageField as ResizedImageFormField


class ResizedImageField(ImageField):

    def formfield(self, **kwargs):
        defaults = {'form_class': ResizedImageFormField}
        defaults.update(kwargs)
        return super(ResizedImageField, self).formfield(**defaults)
