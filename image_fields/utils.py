from PIL import Image

try:
    from io import BytesIO
except ImportError:
    try:
        from cStringIO import StringIO as BytesIO
    except ImportError:
        from StringIO import StringIO as BytesIO


def resize_image(image, size, content_type, quality=98, file_path=None):
    image.thumbnail(size, Image.ANTIALIAS)
 
    if not file_path:
        save_to = BytesIO()
    else:
        save_to = file_path

    image.save(
        save_to,
        quality=quality,
        format=content_type
    )
    return save_to
