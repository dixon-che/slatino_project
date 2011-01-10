from slatino.apps.Institute.models import Institute, Occupation, OccupationPeriod
from django.contrib import admin
from django.conf import settings


class InlineOccupation(admin.TabularInline):
    model = Occupation

class InlineOccupationPeriod(admin.TabularInline):
    model = OccupationPeriod

class InstituteAdmin(admin.ModelAdmin):
    list_display=('id', 'pub_date', 'name', 'work_time', 'adres', 'pub_date', 'publisher')
    inlines = [InlineOccupation, ]

    class Media:
        js = (settings.MEDIA_URL + 'tiny_mce/tiny_mce.js',
              settings.MEDIA_URL + 'tiny_mce/textarea.js',
              )
admin.site.register(Institute, InstituteAdmin)

class OccupationAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'institute')
    inlines = [InlineOccupationPeriod, ]

    #class Media:
    #    js = (settings.MEDIA_URL + '/tiny_mce/tiny_mce.js',
    #          settings.MEDIA_URL + '/tiny_mce/textarea.js',
    #          )

admin.site.register(Occupation, OccupationAdmin)

