from django import forms
from django.conf import settings


class CustomAdminDateWidget(forms.DateInput):

    class Media:
        js = (settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
              settings.MEDIA_URL + "widgets/DateTimeShortcuts.js")

    def __init__(self, attrs={}, format=None):
        super(CustomAdminDateWidget, self).__init__(attrs={'class': 'vDateField', 'size': '10'}, format=format)
