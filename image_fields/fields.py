from django.db.models.fields.files import ImageField

from . import forms


class ResizedImageField(ImageField):

    def __init__(self, *args, **kwargs):
        self.required_size = kwargs.pop('required_size', None)
        self.image_quality = kwargs.pop('image_quality', None)
        super(ResizedImageField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(ImageField, self).deconstruct()
        if self.required_size:
            kwargs['required_size'] = self.required_size
        if self.image_quality:
            kwargs['image_quality'] = self.image_quality
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.ResizedImageField}
        if self.required_size:
            kwargs['required_size'] = self.required_size
        if self.image_quality:
            kwargs['image_quality'] = self.image_quality
        defaults.update(kwargs)
        return super(ResizedImageField, self).formfield(**defaults)
