from slatino.Institute.models import Institute, Room
from django.contrib import admin
from django.conf import settings


class InstituteAdmin(admin.ModelAdmin):
    list_display=('id', 'pub_date', 'name', 'work_time', 'adres', 'pub_date', 'publisher')

    class Media:
        js = (settings.MEDIA_URL + 'tiny_mce/tiny_mce.js',
              settings.MEDIA_URL + 'tiny_mce/textarea.js',
              )
admin.site.register(Institute, InstituteAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display=('id', 'pub_date', 'institute')

    class Media:
        js = (settings.MEDIA_URL + '/tiny_mce/tiny_mce.js',
              settings.MEDIA_URL + '/tiny_mce/textarea.js',
              )
admin.site.register(Room, RoomAdmin)
