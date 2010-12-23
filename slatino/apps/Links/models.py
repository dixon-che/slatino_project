from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from tagsfield.models import Tag
from tagsfield import fields


class Links(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    publisher = models.ForeignKey(User)
    tags = fields.TagsField(Tag)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return "/links/%d/" % self.id


    
