from django.test import TestCase
from .utils import create_question


class ImageFieldsTestCase(TestCase):
    def setUp(self):
        super(ImageFieldsTestCase, self).setUp()
        self.question = create_question(self)
