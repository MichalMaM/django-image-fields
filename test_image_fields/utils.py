from PIL import Image, ImageDraw

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
    return create_obj(Question, defaults=defaults, **kwargs)


def create_image(file_path, size=(1000, 1000), text="Hello World!", text_position=(10,10), color=(255,0,0), file_type="jpeg"):

    im = Image.new('RGB', size)
    draw = ImageDraw.Draw(im)

    draw.text(text_position, text, fill=color)

    del draw

    image = im.save(file_path, file_type)

    return image
