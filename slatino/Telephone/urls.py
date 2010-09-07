from django.conf.urls.defaults import *

urlpatterns = patterns('slatino.Telephone.views',
    url(r'^$', 'telephone_list', name='telephone-list'),
)
