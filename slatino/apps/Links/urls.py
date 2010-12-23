from django.conf.urls.defaults import *

urlpatterns = patterns('slatino.apps.Links.views',
    url(r'^$', 'links_list', name='links-list'),
    url(r'^(?P<link_id>\d+)/$', 'link_show', name='link-show'),
    #url(r'^(?P<slug>\w+)/$', 'news_show_spec'),
)
