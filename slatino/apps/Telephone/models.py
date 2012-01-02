from django.db import models
#from django.core.urlresolvers import reverse
#from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from slatino.apps.Persons.models import Person


from tagsfield.models import Tag
from tagsfield import fields


class Phone(models.Model):
    STATUS_CHOICES = (
        (1, "domashniy"),
        (2, "slugebniy"),
    )
    phone = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    person = models.ForeignKey(Person, related_name='Person')
    pub_date = models.DateTimeField('date published')
    publisher = models.ForeignKey(User)
    tags = fields.TagsField(Tag)

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"

    def __unicode__(self):
        return self.phone

    def get_absolute_url(self):
        return "/phone/%d/" % self.id
