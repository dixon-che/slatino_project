from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to="profile_images", blank=True, null=True)
    first_name = models.CharField(verbose_name=_('First name'), max_length=30, blank=True)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=40, blank=True)
    date_of_birth = models.DateField(verbose_name=_('Date of birth'), blank=True, null=True)
    sex = models.CharField(verbose_name=_('Sex'), choices=(('Male', _('Male')), ('Female', _('Female'))), blank=True, null=True, max_length=6)
    occupation = models.CharField(verbose_name=_('Occupation'), max_length=50, blank=True)
    about = models.TextField(verbose_name=_('About'), max_length=500, help_text="(Some words about yourself.)", blank=True, default="tatata")

    def __unicode__(self):
        return self.user.username
