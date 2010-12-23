from slatino.apps.Telephone.models import Phone
from django.contrib import admin

class PhoneAdmin(admin.ModelAdmin):
    list_display=('id','pub_date','phone')
    #list_filter = ('status')

admin.site.register(Phone, PhoneAdmin)
