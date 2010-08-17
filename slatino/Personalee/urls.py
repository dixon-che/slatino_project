from django.conf.urls.defaults import *

urlpatterns = patterns('slatino.Personalee.views',
    url(r'^$', 'personalee_list'),
    url(r'^(?P<personalee_id>\d+)/$', 'personalee_show'),
    url(r'^(?P<slug>\w+)/$', 'personalee_show_spec'),
)
