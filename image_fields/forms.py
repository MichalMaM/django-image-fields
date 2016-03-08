import os
import sys
from django.forms.fields import ImageField

from .utils import resize_image, BytesIO, Image
from . import conf


class ResizedImageField(ImageField):

    def __init__(self, *args, **kwargs):
        self.required_size = kwargs.pop('required_size', conf.DEFAULT_IMAGE_SIZE)
        self.image_quality = kwargs.pop('image_quality', conf.DEFAULT_IMAGE_QUALITY)
        super(ResizedImageField, self).__init__(*args, **kwargs)


    def to_python(self, data):
        f = super(ResizedImageField, self).to_python(data)
        
        if f is None:
            return None

        data_width, data_height = data.image.size

        if data_width > self.required_size[0] or data_height > self.required_size[1]:

            if hasattr(data, 'temporary_file_path'):
                file = data.temporary_file_path()
                file_path = file
            else:
                file_path = None
                if hasattr(data, 'read'):
                    file = BytesIO(data.read())
                else:
                    file = BytesIO(data['content'])

            image = Image.open(file)

            resized_data = resize_image(
                image,
                self.required_size,
                data.image.format,
                quality=self.image_quality,
                file_path=file_path
            )

            # close original image
            f.image.close()
            # add resized image
            f.image = image

            if not file_path:
                f.file = resized_data
                f.size = sys.getsizeof(resized_data)
            else:
                f.size = os.path.getsize(resized_data)

        return f
