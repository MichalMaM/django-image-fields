import os
from PIL import Image
from nose import tools

from image_fields.utils import resize_image
from .cases import ImageFieldsTestCase


class TestResizeImage(ImageFieldsTestCase):

    def setUp(self):
        super(TestResizeImage, self).setUp()
        self.medium_image_resized_path = os.path.join('data', 'medium_image_resized.jpg')

    def tearDown(self):
        super(TestResizeImage, self).tearDown()
        if os.path.exists(self.medium_image_resized_path):
            os.remove(self.medium_image_resized_path)

    def test_image_is_resized_for_mem_target_size_200_200(self):
        image_path = os.path.join('data', 'medium_image.jpg')
        with Image.open(image_path) as im:
            new_mem_file = resize_image(im, size=(200, 200), content_type=im.format)
            tools.assert_equals(im.size, (200, 93))

        with Image.open(new_mem_file) as im:
            tools.assert_equals(im.size, (200, 93))

    def test_image_is_resized_for_disk_file_target_size_200_200(self):
        image_path = os.path.join('data', 'medium_image.jpg')
        with Image.open(image_path) as im:
            new_file_path = resize_image(im, size=(200, 200), content_type=im.format, file_path=self.medium_image_resized_path)
            tools.assert_equals(im.size, (200, 93))
            tools.assert_equals(new_file_path, self.medium_image_resized_path)

        with Image.open(new_file_path) as im:
            tools.assert_equals(im.size, (200, 93))
