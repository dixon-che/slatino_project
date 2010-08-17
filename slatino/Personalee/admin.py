from slatino.Personalee.models import Personalee
from django.contrib import admin

class PersonaleeAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'phone', 'god_rogd', 'date')

    class Media:
        js = ('/tiny_mce/tiny_mce.js',
              '/tiny_mce/textarea.js',
              )
admin.site.register(Personalee, PersonaleeAdmin)
