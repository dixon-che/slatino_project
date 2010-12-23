from django.conf.urls.defaults import *

urlpatterns = patterns('slatino.apps.Institute.views',
    url(r'^$', 'institute_list', name='institute-list'),
    url(r'^(?P<institute_id>\d+)/$', 'institute_show', name='institute-show'),
    url(r'^(?P<slug>\w+)/$', 'institute_show_spec'),
)
