from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
from tagsfield.models import Tag
from tagsfield import fields


class Institute(models.Model):
    name = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255)
    adres = models.TextField()
    pub_date = models.DateTimeField('date published')
    publisher = models.ForeignKey(User)
    institute_image = models.ImageField(upload_to="institute_images")
    template = models.FilePathField(path=settings.ROOT_PATH + "templates", default = "templates/institute_template.html", blank=True)
    about = models.TextField(max_length=500, blank=True)
    mail_adres = models.EmailField(blank=True)
    phone = models.CharField(max_length=55, blank=True)
    links = models.TextField(max_length=500, blank=True)
    tags = fields.TagsField(Tag)

    class Meta:
        verbose_name = "Institute"
        verbose_name_plural = "Institutes"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/institute/%d/" % self.id
		
class Room(models.Model):
    institute = models.ForeignKey(Institute)
    number_room = models.IntegerField()
    chel = models.CharField(max_length=255)
    doljnost = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255)
    work_day = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    publisher = models.ForeignKey(User)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __unicode__(self):
        return self.chel

    def get_absolute_url(self):
        return "/room/%d/" % self.id
