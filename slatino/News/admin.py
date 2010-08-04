from slatino.News.models import News
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
    list_display=('id','pub_date','title')

    class Media:
        js = ('/tiny_mce/tiny_mce.js',
              '/tiny_mce/textarea.js',
              )
admin.site.register(News, NewsAdmin)
