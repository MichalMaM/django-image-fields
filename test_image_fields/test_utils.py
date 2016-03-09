import os
from PIL import Image
from nose import tools

from image_fields.utils import resize_image
from .cases import ImageFieldsTestCase


class TestResizeImage(ImageFieldsTestCase):

    def test_image_is_resized_for_mem_target_size_200_200(self):
        image_path = os.path.join('data', 'medium_image.jpg')
        with Image.open(image_path) as im:
            new_image = resize_image(im, size=(200, 200), content_type=im.format)
            tools.assert_equals(im.size, (200, 93))
