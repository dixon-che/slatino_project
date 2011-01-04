from slatino.apps.Personalee.models import Personalee
from django.contrib import admin

class PersonaleeAdmin(admin.ModelAdmin):
    list_display=('id', 'first_name', 'date_of_birth', 'occupation', 'phone', 'about')

    class Media:
        js = ('/tiny_mce/tiny_mce.js',
              '/tiny_mce/textarea.js',
             )
admin.site.register(Personalee, PersonaleeAdmin)
