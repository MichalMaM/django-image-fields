import os
from PIL import Image, ImageDraw

from django.core.files.uploadedfile import InMemoryUploadedFile

from test_image_fields.models import Question


def create_obj(model, defaults, commit=True, **kwargs):
    defaults.update(kwargs)
    obj = model(**defaults)
    if commit:
        obj.save()
    return obj


def create_question(test_case, **kwargs):
    defaults = dict(
        question_text="Test text question",
    )
    obj = create_obj(Question, defaults=defaults, commit=False, **kwargs)
    image_field = Question._meta.get_field('image')

    file_path = kwargs.pop('file_path', os.path.join('data', 'small_image.jpg'))

    with open(file_path, 'rb') as f:
        upload_file = InMemoryUploadedFile(
            file=f,
            field_name='image',
            name='medium_image.jpg',
            content_type='image/jpeg',
            size=os.path.getsize(file_path),
            charset=None
        )
        image_field.save_form_data(obj, upload_file)
        obj.save()
    return obj


def create_image(file_path, size=(1000, 1000), text="Hello World!", text_position=(10, 10), color=(255, 0, 0), file_type="jpeg"):

    im = Image.new('RGB', size)
    draw = ImageDraw.Draw(im)

    draw.text(text_position, text, fill=color)

    del draw

    image = im.save(file_path, file_type)

    return image
