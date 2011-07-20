import re
from django.db import models
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext_lazy as _
from django.forms import ValidationError
from django.forms.fields import CharField as formCharField
from django.utils.encoding import smart_unicode
from django.conf import settings
from slatino.apps.Tagsfield.models import Tag
from slatino.apps.Tagsfield import fields
from slatino.apps.Persons.models import Person


class UAPhoneNumberField(formCharField):
    default_error_messages = {
        'invalid': _('Phone numbers must be in +380XXXXXXXXX format.'),
    }

    def clean(self, value):
        super(UAPhoneNumberField, self).clean(value)
        if value in EMPTY_VALUES:
            return u''
        m = re.search('(?<=\+380)\d{9}', smart_unicode(value))
        if m:
            value = m.group(0)
            return u'+380%s' % value
        raise ValidationError(self.error_messages['invalid'])


class PhoneNumberField(models.CharField):

    description = _("Phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 13
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': UAPhoneNumberField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)


class Institute(models.Model):
    name = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255)
    adres = models.TextField()
    institute_image = models.ImageField(upload_to="institute_images")
    template = models.FilePathField(path=settings.ROOT_PATH + "templates", default="templates/institute_template.html", blank=True)
    about = models.TextField(max_length=500, blank=True)
    mail_adres = models.EmailField(blank=True)
    phone = models.CharField(max_length=55, blank=True)
    links = models.TextField(max_length=500, blank=True)
    published = models.BooleanField(default=False)
    tags = fields.TagsField(Tag)

    class Meta:
        verbose_name = "Institute"
        verbose_name_plural = "Institutes"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/institute/%d/" % self.id


class Occupation(models.Model):
    institute = models.ForeignKey(Institute)
    person = models.ManyToManyField(Person, through='OccupationPeriod', related_name='occupations')
    name = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255)
    work_days = models.CharField(max_length=255)
    phone = PhoneNumberField()

    class Meta:
        verbose_name = "Occupation"
        verbose_name_plural = "Occupations"

    def __unicode__(self):
        return self.name


class OccupationPeriod(models.Model):
    occupation = models.ForeignKey(Occupation)
    person = models.ForeignKey(Person)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
