from django.contrib import admin
from dcdjutils.Articles.models import Article, ArticleDescription, ArticlePhoto
from django.conf import settings


class ArticleInlineDescription(admin.StackedInline):
    model = ArticleDescription
    max_num = len(settings.LANGUAGES)
    extra = len(settings.LANGUAGES)

    fields = ('lang', 'title', 'description', 'published')


class ArticleAdmin(admin.ModelAdmin):
    list_display=('slug', 'name', 'pub_date', 'post_type')
    prepopulated_fields = {"slug": ("name", )}

    inlines = [ArticleInlineDescription, ]

    class Media:
        js = ('/tiny_mce/tiny_mce.js',
              '/articles-media/dcarticletextarea.js',
              )


class ArticlePhotoAdmin(admin.ModelAdmin):
    list_display=('id', 'article', 'stamp')


admin.site.register(ArticlePhoto, ArticlePhotoAdmin)
admin.site.register(Article, ArticleAdmin)
