from slatino.apps.Personalee.models import Personalee
from django.contrib import admin
from slatino.apps.Institute.models import OccupationPeriod

class InlineOccupation(admin.TabularInline):
    model = OccupationPeriod

class PersonaleeAdmin(admin.ModelAdmin):
    list_display=('id', 'last_name', 'first_name', 'date_of_birth', 'occupation', 'phone')
    inlines = [InlineOccupation, ]

    class Media:
        js = ('/tiny_mce/tiny_mce.js',
              '/tiny_mce/textarea.js',
             )
admin.site.register(Personalee, PersonaleeAdmin)
