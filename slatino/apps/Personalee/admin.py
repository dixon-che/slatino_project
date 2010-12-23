from slatino.apps.Personalee.models import Personalee
from django.contrib import admin

#class PersonaleeAdmin(admin.ModelAdmin):
#    list_display=('id', 'first_name', 'phone', '', 'date')
#
#    class Media:
#        js = ('/tiny_mce/tiny_mce.js',
#              '/tiny_mce/textarea.js',
#             )
admin.site.register(Personalee)
