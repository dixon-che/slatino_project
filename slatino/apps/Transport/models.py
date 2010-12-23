from django.db import models
from django.core.urlresolvers import reverse
from slatino.apps.Personalee.models import Personalee


from tagsfield.models import Tag
from tagsfield import fields


class Transport(models.Model):
    vid = models.CharField(max_length=55)
    napravlenie = models.CharField(max_length=55)
   # personalee = models.ForeignKey(Personalee, related_name='Personalee' )
    description = models.TextField()
    tags = fields.TagsField(Tag)

    class Meta:
        verbose_name = "Transport"
        verbose_name_plural = "Transports"

    def __unicode__(self):
        return self.vid

    def get_absolute_url(self):
        return "/transport/%d/" % self.id

class Raspisanie(models.Model):
    otpravlenie = models.CharField(max_length=55)
    pribitie = models.CharField(max_length=55)
    transport = models.ForeignKey(Transport)
	
    def __unicode__(self):
        return self.otpravlenie
		
    def get_absolute_url(self):
        return "/raspisanie/%d/" % self.id
	
class Ceni(models.Model):
    marshrut = models.CharField(max_length=255)
    cena = models.CharField(max_length=55)
    transport = models.ForeignKey(Transport)
	
    def __unicode__(self):
        return self.marshrut
