from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from tagsfield.models import Tag
from tagsfield import fields


class Personalee(models.Model):
    name = models.CharField(max_length=155)
    god_rogd = models.CharField(max_length=55)
    phone= models.CharField(max_length=55)
    description = models.TextField()
    date = models.DateTimeField('date published')
    publisher = models.ForeignKey(User)
    personalee_image = models.ImageField(upload_to="personalee_images")
    tags = fields.TagsField(Tag)

    class Meta:
        verbose_name = "Personalee"
        verbose_name_plural = "Personalees"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/personalee/%d/" % self.id
