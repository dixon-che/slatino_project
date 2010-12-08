from django.conf.urls.defaults import *


urlpatterns = patterns('slatino.Publications.views',
    url(r'^last/$', 'publication_last', name='publication-last'),
    url(r'^news/$', 'publication_list', { 'post_type': 'news' }, name='news'),
    url(r'^articles/$', 'publication_list', { 'post_type': 'article' }, name='article'),
    url(r'^view/(?P<publication_slug>[-\w]+)/$', 'publication_view', name='publication-view'),
    #url(r'^(?P<article_id>\d+)/past_image/$', 'past_image'),
    #url(r'^image/(?P<image_id>\d+)/$', 'image_view', name='article-image-view'),
    #url(r'^image/(?P<image_id>\d+)/(?P<size>\d+)/$', 'image_view', name='article-image-view-thumb'),
)
