from slatino.Institute.models import Institute, Room
from django.contrib import admin

class InstituteAdmin(admin.ModelAdmin):
    list_display=('id','pub_date','name','work_time','adres','pub_date','publisher')

    class Media:
        js = ('/tiny_mce/tiny_mce.js',
              '/tiny_mce/textarea.js',
              )
admin.site.register(Institute, InstituteAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display=('id','pub_date','institute')

    class Media:
        js = ('/tiny_mce/tiny_mce.js',
              '/tiny_mce/textarea.js',
              )
admin.site.register(Room, RoomAdmin)
