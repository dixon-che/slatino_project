from django.conf.urls.defaults import *

urlpatterns = patterns('slatino.Transport.views',
    url(r'^$', 'transport_list', name='transport-list'),
    url(r'^(?P<raspisanie_id>\d+)/$', 'raspisanie_show', name='raspisanie-show'),
    url(r'^ceni/$', 'ceni_show', name='ceni-show'),
)
