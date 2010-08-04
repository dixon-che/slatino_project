from slatino.Links.models import Links
from django.contrib import admin

class LinksAdmin(admin.ModelAdmin):
    list_display=('id','link', 'title', 'publisher', 'pub_date')

admin.site.register(Links, LinksAdmin)

