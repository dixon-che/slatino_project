from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import translation
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from slatino.apps.Publications.utils import get_cache_file_url

from tagsfield.models import Tag
from tagsfield import fields


class Publication(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    post_type = models.CharField(max_length=20, choices=settings.POST_TYPES, default='article')
    publisher = models.ForeignKey(User)
    pub_date = models.DateTimeField(_(u'Date published'))
    order = models.IntegerField(_(u'Order'), default=50)
    published = models.BooleanField(default=False)
    tags = fields.TagsField(Tag)

    class Meta:
        verbose_name = _(u"Publication")
        verbose_name_plural = _(u"Publications")

    def __unicode__(self):
        return self.name

    def _get_data(self):
        publicationdescriptions = self.publicationdescription_set.filter(lang=translation.get_language(), published=True)
        if publicationdescriptions:
            return publicationdescriptions[0]
        publicationdescriptions = self.publicationdescription_set.filter(lang=settings.DEFAULT_LANG, published=True)
        if publicationdescriptions:
            return publicationdescriptions[0]
        publicationdescriptions = self.publicationdescription_set.filter(published=True)
        if publicationdescriptions:
            return publicationdescriptions[0]

    data = property(_get_data)

    def _get_title(self):
        return self.data.title
    title = property(_get_title)

    def _get_description(self):
        return self.data.description
    description = property(_get_description)

    def get_url(self):
        #print reverse('publication-view', kwargs={'publication_slug': self.slug})
        return reverse('publication-view', args=[self.slug])

    def get_absolute_url(self):
        #print reverse('publication-view', args=[self.slug])
        return reverse('publication-view', args=[self.slug])

    def get_images(self):
        return  PublicationPhoto.objects.filter(publication=self)

    def get_verbose_post_type(self):
        post_type_dict = dict(settings.POST_TYPES)
        return post_type_dict[self.post_type]


class PublicationDescription(models.Model):
    base = models.ForeignKey(Publication)
    title = models.CharField(max_length=255)
    description = models.TextField()
    lang = models.CharField(choices=settings.LANGUAGES, max_length=5)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"Publication")
        verbose_name_plural = _(u"Publications")

        unique_together = (("base", "lang"), )


class PublicationPhoto(models.Model):
    publication = models.ForeignKey(Publication)
    image = models.ImageField(upload_to="publication_images")
    stamp = models.DateTimeField(auto_now=True)

    def get_url_with_id(self):
        return reverse('publication-image-view', self.id)

    def thumbnail_size(self):
        return 300

    def thumbnail_url(self, size):
        return get_cache_file_url(self, "publication_images/thumbnails", size)
