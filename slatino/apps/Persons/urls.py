from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('slatino.apps.Persons.views',
    url(r'^$', 'person_list', name='person-list'),
    url(r'^(?P<person_id>\d+)/$', 'person_show'),
    url(r'^(?P<slug>\w+)/$', 'person_show_spec'),
)
