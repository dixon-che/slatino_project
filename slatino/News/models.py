from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from tagsfield.models import Tag
from tagsfield import fields


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    publisher = models.ForeignKey(User)
    news_image = models.ImageField(upload_to="news_images")
    tags = fields.TagsField(Tag)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/news/%d/" % self.id
