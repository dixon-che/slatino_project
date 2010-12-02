from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    #photo = models.ImageField(upload_to=None, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(choices=(('Male', 'Male'), ('Female', 'Female')), blank=True, null=True, max_length=6)
    occupation = models.CharField(max_length=50, blank=True)
    about = models.TextField(max_length=500, help_text="(Some words about yourself.)", blank=True, default="tatata")

    def __unicode__(self):
        return self.user.username
