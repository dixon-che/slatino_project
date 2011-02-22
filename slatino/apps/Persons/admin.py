from slatino.apps.Persons.models import Person
from django.contrib import admin
from slatino.apps.Institute.models import OccupationPeriod
from slatino.utils.widgets import CustomAdminDateWidget
from django.db import models
from django.conf import settings


class InlineOccupationPeriod(admin.TabularInline):
    model = OccupationPeriod
    formfield_overrides = {
        models.DateField: {'widget': CustomAdminDateWidget},
    }


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'date_of_birth', 'occupation', 'phone')
#    inlines = [InlineOccupationPeriod, ]
    formfield_overrides = {
        models.DateField: {'widget': CustomAdminDateWidget},
    }

    class Media:
        js = ('/tiny_mce/tiny_mce.js',
              settings.MEDIA_URL + 'Publication-media/dcarticletextarea.js',
             )
admin.site.register(Person, PersonAdmin)
