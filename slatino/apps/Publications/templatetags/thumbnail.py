import os
import Image
from django.template import Library
from django.conf import settings

register = Library()


def thumbnail(file, size='300x300'):
    # defining the size
    filename = str(file)
    x, y = [int(x) for x in size.split('x')]
    # defining the filename and the miniature filename

    basename, file_format = filename.rsplit('.', 1)
    folder, name = basename.rsplit('/', 1)
    miniature = folder + '/thumbnail/' + name + '_' + size + '.' + file_format
    #miniature_nomedia = miniature[len(settings.MEDIA_URL):]
    #file_nomedia = file[len(settings.MEDIA_URL):]

    filename = settings.MEDIA_ROOT + "/" + filename
    miniature_filename = settings.MEDIA_ROOT + "/" + miniature
    miniature_url = settings.MEDIA_URL + miniature
    if os.path.exists(miniature_filename) and os.path.getmtime(filename)>os.path.getmtime(miniature_filename):
        os.unlink(miniature_filename)
    # if the image wasn't already resized, resize it
    if not os.path.exists(miniature_filename):
        image = Image.open(filename)
        image.thumbnail([x, y], Image.ANTIALIAS)
        image.save(miniature_filename, image.format)
    return miniature_url


register.filter(thumbnail)
