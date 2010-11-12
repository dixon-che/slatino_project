from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import translation
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from dcdjutils.Articles.utils import get_cache_file_url

from tagsfield.models import Tag
from tagsfield import fields


class Article(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    post_type = models.CharField(max_length=20, choices=settings.POST_TYPES)
    publisher = models.ForeignKey(User)
    pub_date = models.DateTimeField(_(u'Date published'))
    order = models.IntegerField(_(u'Order'), default=50)
    published = models.BooleanField(default=False)
    tags = fields.TagsField(Tag)

    class Meta:
        verbose_name = _(u"Article")
        verbose_name_plural = _(u"Articles")

    def __unicode__(self):
        return self.name

    def _get_data(self):
        articledescriptions = self.articledescription_set.filter(lang=translation.get_language(), published=True)
        if articledescriptions:
            return articledescriptions[0]
        articledescriptions = self.articledescription_set.filter(lang=settings.DEFAULT_LANG, published=True)
        if articledescriptions:
            return articledescriptions[0]
        articledescriptions = self.articledescription_set.filter(published=True)
        if articledescriptions:
            return articledescriptions[0]

    data = property(_get_data)

    def _get_title(self):
        return self.data.title
    title = property(_get_title)

    def _get_description(self):
        return self.data.description
    description = property(_get_description)

    def get_absolute_url(self):
        return reverse('article-view', args=[self.slug])

    def get_images(self):
        return  ArticlePhoto.objects.filter(article=self)


class ArticleDescription(models.Model):
    base = models.ForeignKey(Article)
    title = models.CharField(max_length=255)
    description = models.TextField()
    lang = models.CharField(choices=settings.LANGUAGES, max_length=5)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"Article")
        verbose_name_plural = _(u"Articles")

        unique_together = (("base", "lang"), )


class ArticlePhoto(models.Model):
    article = models.ForeignKey(Article)
    image = models.ImageField(upload_to="article_images/")
    stamp = models.DateTimeField(auto_now=True)

    def get_url_with_id(self):
        return reverse('article-image-view', self.id)

    def thumbnail_size(self):
        return 300

    def thumbnail_url(self, size):
        return get_cache_file_url(self, "article_images/thumbnails", size)
