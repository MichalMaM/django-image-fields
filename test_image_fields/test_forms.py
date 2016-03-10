from __future__ import unicode_literals

import os
from PIL import Image
from nose import tools

from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile

from image_fields.forms import ResizedImageField

from .cases import ImageFieldsTestCase
from .utils import get_full_file_path


class TestResizedImageField(ImageFieldsTestCase):

    def test_image_is_resized_for_setting_size(self):
        image_path = get_full_file_path(os.path.join('data', 'medium_image.jpg'))

        with open(image_path, 'rb') as f:
            upload_file = InMemoryUploadedFile(
                file=f,
                field_name='image',
                name='medium_image.jpg',
                content_type='image/jpeg',
                size=os.path.getsize(image_path),
                charset=None
            )
            image_field = ResizedImageField()
            new_image = image_field.clean(upload_file)

            tools.assert_not_equals(f, new_image.file)

            with Image.open(new_image) as im:
                tools.assert_equals(im.size, (300, 140))

    def test_image_is_resized_for_setting_size_and_big_image(self):
        image_path = get_full_file_path(os.path.join('data', 'big_image.jpg'))

        with open(image_path, 'rb') as f:
            upload_file = TemporaryUploadedFile(
                name='medium_image.jpg',
                content_type='image/jpeg',
                size=os.path.getsize(image_path),
                charset=None
            )
            upload_file.write(f.read())
            image_field = ResizedImageField()
            new_image = image_field.clean(upload_file)

            tools.assert_not_equals(f, new_image.file)

            with Image.open(new_image) as im:
                tools.assert_equals(im.size, (300, 150))

    def test_image_is_resized_for_kwargs_spec_size(self):
        image_path = get_full_file_path(os.path.join('data', 'medium_image.jpg'))

        with open(image_path, 'rb') as f:
            upload_file = InMemoryUploadedFile(
                file=f,
                field_name='image',
                name='medium_image.jpg',
                content_type='image/jpeg',
                size=os.path.getsize(image_path),
                charset=None
            )
            image_field = ResizedImageField(required_size=(200, 200))
            new_image = image_field.clean(upload_file)

            tools.assert_not_equals(f, new_image.file)

            with Image.open(new_image) as im:
                tools.assert_equals(im.size, (200, 93))

    def test_image_is_not_resized_if_is_smaller_than_bounds(self):
        image_path = get_full_file_path(os.path.join('data', 'small_image.jpg'))

        with open(image_path, 'rb') as f:
            upload_file = InMemoryUploadedFile(
                file=f,
                field_name='image',
                name='medium_image.jpg',
                content_type='image/jpeg',
                size=os.path.getsize(image_path),
                charset=None
            )
            image_field = ResizedImageField()
            new_image = image_field.clean(upload_file)

            tools.assert_equals(f, new_image.file)

            with Image.open(new_image) as im:
                tools.assert_equals(im.size, (100, 50))

    @tools.raises(forms.ValidationError)
    def test_image_raise_validation_error_if_file_is_not_image(self):
        image_path = get_full_file_path(os.path.join('data', 'hi.txt'))

        with open(image_path, 'rb') as f:
            upload_file = InMemoryUploadedFile(
                file=f,
                field_name='image',
                name='medium_image.jpg',
                content_type='image/jpeg',
                size=os.path.getsize(image_path),
                charset=None
            )
            image_field = ResizedImageField()
            image_field.clean(upload_file)

    def test_return_none_if_image_does_not_changed(self):
        image_path = get_full_file_path(os.path.join('data', 'small_image.jpg'))

        with open(image_path, 'rb') as f:
            image_field = ResizedImageField()
            new_image = image_field.clean(None, initial=f)

            tools.assert_not_equals(None, new_image)
