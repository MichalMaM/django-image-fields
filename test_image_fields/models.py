from __future__ import unicode_literals

from django.utils.encoding import force_text, python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return force_text(self.pk)
