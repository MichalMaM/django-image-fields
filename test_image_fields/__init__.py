from os import environ
import django

environ['DJANGO_SETTINGS_MODULE'] = 'test_image_fields.settings'

test_runner = None
old_config = None

django.setup()


def setup():
    global test_runner
    global old_config

    from django.test.runner import DiscoverRunner

    test_runner = DiscoverRunner()
    test_runner.setup_test_environment()
    old_config = test_runner.setup_databases()


def teardown():
    from shutil import rmtree
    from django.conf import settings
    test_runner.teardown_databases(old_config)
    test_runner.teardown_test_environment()
    rmtree(settings.MEDIA_ROOT, ignore_errors=True)
