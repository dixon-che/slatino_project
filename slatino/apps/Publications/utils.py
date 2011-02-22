import Image
import os
from datetime import datetime
from stat import *
from django.conf import settings


def make_thumbnail(image_object, result_file, x, y=None):
    if y is None:
        y = x
    im = Image.open(image_object.image.path)
    im.thumbnail((int(x), int(y)), Image.ANTIALIAS)
    if im.mode != "RGB":
        im = im.convert("RGB")
    im.save(result_file, "JPEG")


def parse_str2datetime(date_string):
    a, b = date_string.split(' ')
    Y, M, D = a.split("-")
    h, m, s = b.split(":")
    return datetime(int(Y), int(M), int(D), int(h), int(m), int(s))


def in_cache(full_filename, src_modtime):
    if os.path.exists(full_filename):
        dst_modtime = datetime.fromtimestamp(os.stat(full_filename)[ST_MTIME])
        if dst_modtime < src_modtime:
            return False
        return True
    return False


def get_cache_file_url(image_object, thumbnail_dir, size):
    file_suff = thumbnail_dir + '/' + str(image_object.id) + '_' + str(size) + '.jpg'

    result_file = settings.MEDIA_ROOT + '/' + file_suff

    result_file_url = settings.MEDIA_URL + file_suff

    if not in_cache(result_file, image_object.stamp):
        make_thumbnail(image_object, result_file, size)

    return result_file_url
