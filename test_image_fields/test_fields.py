from nose import tools

from .cases import ImageFieldsTestCase

from image_fields.fields import ResizedImageField
from image_fields import forms


class TestResizedImageField(ImageFieldsTestCase):

    def test_image_is_set_correct(self):
        image_field = self.question._meta.get_field('image')
        tools.assert_equals((self.question.image.width, self.question.image.height), (100, 50))
        tools.assert_true(isinstance(image_field, ResizedImageField))

    def test_correct_form_field_is_returned(self):
        image_field = self.question._meta.get_field('image')
        tools.assert_true(isinstance(image_field.formfield(), forms.ResizedImageField))

    def test_correct_size_quality_for_form_field(self):
        size = (500, 500)
        quality = 95

        image_field = ResizedImageField(required_size=size, image_quality=quality)
        image_form_field = image_field.formfield()
        deconstruct_kwargs = image_field.deconstruct()[-1]

        tools.assert_true(isinstance(image_form_field, forms.ResizedImageField))
        tools.assert_equals(image_form_field.required_size, size)
        tools.assert_equals(image_form_field.image_quality, quality)
        tools.assert_equals(deconstruct_kwargs['required_size'], size)
        tools.assert_equals(deconstruct_kwargs['image_quality'], quality)
