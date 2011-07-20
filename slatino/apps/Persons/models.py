from django.db import models
from slatino.apps.Tagsfield.models import Tag
from slatino.apps.Tagsfield import fields


class Person(models.Model):
    photo = models.ImageField(upload_to="person_images", blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(choices=(('Male', 'Male'), ('Female', 'Female')), blank=True, null=True, max_length=6)
    occupation = models.CharField(max_length=50, blank=True)
    about = models.TextField(max_length=500, help_text="(Some words about yourself.)", blank=True)
    phone = models.CharField(max_length=55, blank=True)
    tags = fields.TagsField(Tag)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __unicode__(self):
        return u'%s %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return "/person/%d/" % self.id

    def get_occupations_list(self):
        return self.occupationperiod_set.all().order_by('date_start')
