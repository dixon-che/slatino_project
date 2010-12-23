from slatino.apps.Transport.models import Transport, Raspisanie, Ceni
from django.contrib import admin

class TransportAdmin(admin.ModelAdmin):
    list_display=('id','vid', 'napravlenie')

class RaspisanieAdmin(admin.ModelAdmin):
    list_display=('id','otpravlenie','pribitie')

class CeniAdmin(admin.ModelAdmin):
    list_display=('id','marshrut','cena')

admin.site.register(Transport, TransportAdmin)
admin.site.register(Raspisanie, RaspisanieAdmin)
admin.site.register(Ceni, CeniAdmin)
